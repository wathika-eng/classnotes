from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    pass
    # def __init__(self, *args, **kwargs):
    #     kwargs.setdefault("widget", MultipleFileInput())
    #     super().__init__(*args, **kwargs)

    # def clean(self, data, initial=None):
    #     single_file_clean = super().clean
    #     if isinstance(data, (list, tuple)):
    #         result = [single_file_clean(d, initial) for d in data]
    #     else:
    #         result = single_file_clean(data, initial)
    #     return result
    
class NoteForm(forms.ModelForm):
    file = MultipleFileField()
    
    class Meta:
        model = Note
        fields = '__all__'
        # exclude = ['department', 'unit_topic']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'course']  # Fields to be displayed in the form

    def __init__(self, *args, **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)
        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['course'].queryset = Course.objects.filter(id=course_id)
            except (ValueError, TypeError, Course.DoesNotExist):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = Course.objects.filter(id=self.instance.course_id)
