import os
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

DEPARTMENT_CHOICES = [
    ('A', 'Department A'),
    ('B', 'Department B'),
    # Add more departments as needed
]

YEAR_CHOICES = [
    ("1", 'First Year'),
    ("2", 'Second Year'),
    ("3", 'Third Year'),
    ("4", 'Fourth Year'),
    # Add more years as needed
]

SEM_CHOICES = (
    ("1", "First Semester"),
    ("2", "Second Semester")
)

# Choices for Courses
COURSE_CHOICES = [
    ('A1', 'Course A1'),
    ('A2', 'Course A2'),
    ('B1', 'Course B1'),
    ('B2', 'Course B2'),
    # Add more courses as needed
]


def note_file_path(instance, filename):
    # Generate the file path based on the title and original file extension
    ext = filename.split('.')[-1]
    filename = f"{instance.title}.{ext}"
    return os.path.join('media/', filename)


class College(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# Model for School
class School(models.Model):
    name = models.CharField(max_length=50)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='schools')

    def __str__(self):
        return self.name


# Model for Department
class Department(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name


# Model for Course
class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    def get_display_name(self):
        """
        Return the formatted display name as specified.
        """
        return f"{self.name.capitalize()} Notes"

    def __str__(self):
        return self.get_display_name()

    class Meta:
        unique_together = ['name', 'department']


# Model for Units
class Unit(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='units')
    year_of_study = models.CharField(max_length=20, null=True, choices=YEAR_CHOICES)  # Added year of study
    sem = models.CharField(max_length=20, null=True, choices=SEM_CHOICES)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='units')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_display_name(self):
        return f"{self.course.name.upper()}: {self.name} {self.year_of_study}.{self.sem}"

    def __str__(self):
        return self.get_display_name()

    class Meta:
        unique_together = ['name', 'course', 'year_of_study']


class UnitTopic(models.Model):
    """
    Add a Unit Topic name eg: Linear Regression
    """
    name = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='unit_topics')

    def get_display_name(self):
        return f"{self.unit.name.upper()}:{self.name}"

    def __str__(self):
        return self.get_display_name()

    class Meta:
        unique_together = ["name", "unit"]


class Note(models.Model):
    """
    Takes in a Note file for a particular unit's topic
    """
    title = models.CharField(max_length=50, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=False, related_name='notes')
    file = models.FileField(upload_to='media/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    #     def get_display_name(self):
    #     file_name = os.path.splitext(os.path.basename(self.file.name))[0]
    #     return file_name if self.title is None else self.title

    # def __str__(self):
    #     return self.get_display_name()

    def get_display_name(self):
        if self.title is not None:
            return f"{os.path.basename(self.file.name)}"
        return f"{os.path.basename(self.file.name)}"

    def __str__(self):
        return self.get_display_name()

    class Meta:
        unique_together = (
            ('title', 'unit'),
            ('title', 'file'),
            ('unit', 'file'),
            ('title', 'unit', 'file'),
        )

    def save(self, *args, **kwargs):
        if not self.title:
            # Extract filename without extension and set it as title
            self.title = os.path.splitext(os.path.basename(self.file.name))[0]
        # Update the file name before saving
        if self.file.name != '':
            self.file.name = note_file_path(self, os.path.basename(self.file.name))
        super().save(*args, **kwargs)


class UserRequest(models.Model):
    yourschool = models.CharField(max_length=20, null=True)
    yourcourse = models.CharField(max_length=20, null=True)
    enquiry = models.TextField(blank=True)
