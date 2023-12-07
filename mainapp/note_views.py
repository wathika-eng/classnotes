from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import College, School, Department, Course, Unit, UnitTopic, Note
from collections import defaultdict

def college_details(request, college_id):
    college = get_object_or_404(College, pk=college_id)
    schools = School.objects.filter(college=college)

    context = {
        'college': college,
        'schools': schools
    }
    return render(request, 'mainapp/college_details.html', context)


def school_details(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    departments = Department.objects.filter(school=school)

    context = {
        'school': school,
        'departments': departments
    }
    return render(request, 'mainapp/school_details.html', context)


def department_details(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    courses = Course.objects.filter(department=department)
    context = {
        'department': department,
        'courses': courses
    }
    return render(request, 'mainapp/department_details.html', context)


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    units = Unit.objects.filter(course=course)
    units_by_year = defaultdict(list)
    for unit in units:
        units_by_year[unit.year_of_study].append(unit)
    context = {
        'course': course,
        'units_by_year': dict(units_by_year),
    }
    return render(request, 'mainapp/course_details.html', context)

def year_details(request, year_id):
    year = get_object_or_404(year_of_study, pk=year_id)


def unit_details(request, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id)
    # unit_topics = UnitTopic.objects.filter(unit=unit)
    notes = Note.objects.filter(unit=unit)
    context = {
        'unit': unit,
        # 'unit_topics': unit_topics,
        'notes': notes
    }
    return render(request, 'mainapp/unit_details.html', context)


def unit_topic_details(request, unit_topic_id):
    unit_topic = get_object_or_404(UnitTopic, pk=unit_topic_id)
    notes = Note.objects.filter(unit_topic=unit_topic)

    context = {
        'unit_topic': unit_topic,
        'notes': notes
    }

    return render(request, 'mainapp/unit_topic_details.html', context)


def get_colleges(request):
    
    colleges = College.objects.all()
    college_options = [{'id': college.id, 'name': college.name} for college in colleges]

    return JsonResponse({'colleges': college_options})


def get_schools(request):
    # schools = School.objects.all()
    # school_options = [{'id': school.id, 'name': school.name} for school in schools]
    
    # return JsonResponse({'schools': school_options})
    college_id = request.GET.get('college_id')
    schools = School.objects.filter(college_id=college_id)
    data = [{'id': school.id, 'name': school.name} for school in schools]

    return JsonResponse(data, safe=False)


def get_departments(request):
    school_id = request.GET.get('school_id')
    departments = Department.objects.filter(school_id=school_id)
    data = [{'id': department.id, 'name': department.name} for department in departments]
    return JsonResponse(data, safe=False)


def get_courses(request):
    department_id = request.GET.get('department_id')
    print(f"----------DPT ID: {department_id}-----------")
    courses = Course.objects.filter(department_id=department_id)
    print(f"----------COURSES: {courses}----------")
    data = [{'id': course.id, 'name': course.get_display_name()} for course in courses]
    return JsonResponse(data, safe=False)


def get_units(request):
    course_id = request.GET.get('course_id')
    units = Unit.objects.filter(course_id=course_id)
    data = [{'id': unit.id, 'name': unit.name} for unit in units]
    return JsonResponse(data, safe=False)


@login_required(login_url="login")
def submit_notes(request):
    if request.method == 'POST':
        # Handle form submission, create/update models, and save the note file
        # Replace the following with your actual implementation

        try:
            college_id = request.POST.get('college')
            school_id = request.POST.get('school')
            department_id = request.POST.get('department')
            course_id = request.POST.get('course')
            unit_id = request.POST.get('unit')
            # unit_topic_name = request.POST.get('unit_topic')
            note_title = request.POST.get('title')
            note_file = request.FILES.get('note_file')

            # Create or get existing models based on the form data
            college = College.objects.get(id=college_id)
            school = School.objects.get(id=school_id)
            department = Department.objects.get(id=department_id)
            course = Course.objects.get(id=course_id)
            unit = Unit.objects.get(id=unit_id)

            # Create or update the UnitTopic
            # unit_topic, created = UnitTopic.objects.get_or_create(name=unit_topic_name, unit=unit)

            # Save the Note
            note = Note(title=note_title, file=note_file, uploaded_by=request.user, unit=unit)
            note.save()

            # return redirect('unit_topic_details', unit_topic_id=unit_topic.id)
            return JsonResponse({'success': True, 'message': f"/unit_details/{unit.id}"})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
