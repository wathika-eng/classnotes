import traceback
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django_daraja.mpesa.core import MpesaClient
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Note
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.auth.models import User  # Replace with your User model import


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    context = {"form": form}
    return render(request, "mainapp/register.html", context)


def my_login(request):
    user_json = "anonymous"
    form = CustomAuthenticationForm()
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, message="Logged in successfully")
                return redirect("dashboard")
            else:
                messages.warning(request, message="Invalid username or password")
                user_json = json.dumps({})

    context = {"form": form, "user": user_json}

    return render(request, "mainapp/login.html", context=context)


def submit_request(request):
    if request.method == 'POST':
        yourschool = request.POST.get('yourschool')
        yourcourse = request.POST.get('yourcourse')
        enquiry = request.POST.get('enquiry')
        # Process and save request data to the database
        UserRequest.objects.create(yourschool=yourschool, yourcourse=yourcourse, enquiry=enquiry)
        # Optionally, send email notification to admin or perform other actions
        return redirect('dashboard')  # Redirect to home or another page
    return render(request, 'mainapp/modal.html')  # Render the form again if not a POST request


def my_logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")


# @login_required(login_url="login")
def dashboard(request):
    my_records = Note.objects.all().order_by("-uploaded_at")[:5]
    colleges = College.objects.all()
    schools = School.objects.all()
    departments = Department.objects.filter(school__isnull=False)
    unique_departments = []
    seen_departments = set()

    for department in departments:
        key = (department.name, department.school.name)
        if key not in seen_departments:
            unique_departments.append(department)
            seen_departments.add(key)
    context = {
        "notes": my_records,
        "schools": schools,
        "colleges": colleges,
        'unique_departments': unique_departments,
    }
    return render(request, "mainapp/dashboard.html", context=context)

class FileFieldFormView(FormView):
    form_class = NoteForm
    template_name = "mainapp/create_note.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        files = self.request.FILES.getlist('note_file')
        try:
            for file in files:
                existing_file = Note.objects.filter(title=file.name).first()
                if existing_file:
            # If a file with the same name exists, show a warning message
                    messages.warning(
                        self.request,
                        f"File '{file.name}' already exists. Do you want to overwrite it?"
                        )
                    return JsonResponse({'success': False, 'message': 'File already exists'})
                note = Note(file=file, uploaded_by=self.request.user, unit=form.cleaned_data['unit'])
                note.save()
        except Exception as e:
                traceback.print_exc()  # Print the error to console
                # Handle the error as needed
                messages.error(self.request, f"Error uploading file '{file.name}': {e}")

        messages.success(self.request, "Uploaded successfully")
        return super().form_valid(form)
    
def handle_files(f):
    try:
        storage = FileSystemStorage()
        filename = storage.save(f.name, f)
    except Exception as e:
        traceback.print_exc()  # Print the error to console
        # Handle the error as needed

@login_required(login_url="login")
def create_record(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                response = FileFieldFormView
                return response
            except Exception as e:
                traceback.print_exc()  # Print the error to console
                # Handle the error as needed
    else:
        form = NoteForm()
        
    colleges = College.objects.all()
    schools = School.objects.all()
    departments = Department.objects.all()
    courses = Course.objects.all()
    units = Unit.objects.all()

    # Assuming 'department', 'course', 'unit' are the fields in the Note model
    notes = Note.objects.select_related('college', 'school', 'department', 'course', 'unit').all()

    context = {
        'form': form,
        'colleges': colleges,
        'schools': schools,
        'departments': departments,
        'courses': courses,
        'units': units,
        'notes': notes
    }

    return render(request, 'mainapp/create_notes.html', context=context)


def error_404_view(request, exception):
    return redirect("dashboard")


def create_unit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.uploaded_by = request.user  # Set the user who uploaded the unit
            unit.save()
            return redirect('unit_list')  # Redirect to a view or URL name after successful unit creation
    else:
        form = UnitForm()

    return render(request, 'mainapp/unit_create.html', {'form': form})


def send_password_reset_email(request):
    # Logic to identify the user requesting password reset
    user_data = User.objects.get(username='username')  # Example: Get the user object based on a username

    subject = 'Password Reset Request'
    html_message = render_to_string('mainapp/registration/email/password_reset_email.html', {'user': user_data})
    from_email = ''
    recipient_list = [user_data.email]  # Use the user's email address

    send_mail(subject, '', from_email, recipient_list, html_message=html_message)

    return render(request, 'mainapp/registration/password_reset_done.html')

def mpesa(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')  # Get phone number from frontend form
        amount = request.POST.get('amount')  # Get amount from frontend form

        try:
            amount = int(amount)  # Convert the amount string to an integer
        except ValueError:
            return HttpResponse("Invalid amount. Please enter a valid integer amount.")

        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = ''
        previous_url = request.META.get('HTTP_REFERER')
        cl = MpesaClient()
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return render(request, 'mainapp/money.html', {'success_message': 'Payment successful!', 'previous_url': previous_url})

    return render(request, 'mainapp/money.html')