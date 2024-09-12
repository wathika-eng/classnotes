import uuid
from django.db import models
import os
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

DEPARTMENT_CHOICES = [
    ("A", "Department A"),
    ("B", "Department B"),
    # Add more departments as needed
]

YEAR_CHOICES = [
    ("1", "First Year"),
    ("2", "Second Year"),
    ("3", "Third Year"),
    ("4", "Fourth Year"),
    # Add more years as needed
]

SEM_CHOICES = (("1", "First Semester"), ("2", "Second Semester"))

# Choices for Courses
COURSE_CHOICES = [
    ("A1", "Course A1"),
    ("A2", "Course A2"),
    ("B1", "Course B1"),
    ("B2", "Course B2"),
    # Add more courses as needed
]


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault(
            "username", email.split("@")[0]
        )  # Auto-generate username if not provided
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("classrep", "Class Representative"),
        ("moderator", "Moderator"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="student")

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

    class Meta:
        db_table = "auth_user"


def note_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"  # Use UUID for unique filenames
    return os.path.join("media/", filename)


class College(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# Model for School
class School(models.Model):
    name = models.CharField(max_length=50)
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, related_name="schools"
    )

    def __str__(self):
        return self.name


# Model for Department
class Department(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="departments"
    )

    def __str__(self):
        return self.name


# Model for Course
class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="courses"
    )

    def get_display_name(self):
        """
        Return the formatted display name as specified.
        """
        return f"{self.name.capitalize()} Notes"

    def __str__(self):
        return self.get_display_name()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "department"], name="unique_course")
        ]


# Model for Units
class Unit(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")
    year_of_study = models.CharField(
        max_length=20, null=True, choices=YEAR_CHOICES
    )  # Added year of study
    sem = models.CharField(max_length=20, null=True, choices=SEM_CHOICES)
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="units"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_display_name(self):
        return (
            f"{self.course.name.upper()}: {self.name} {self.year_of_study}.{self.sem}"
        )

    def __str__(self):
        return self.get_display_name()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "course", "year_of_study"], name="unique_unit"
            )
        ]


class Note(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, null=True, blank=False, related_name="notes"
    )
    file = models.FileField(upload_to=note_file_path)  # Use the updated path function
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def get_display_name(self):
        return self.title if self.title else os.path.basename(self.file.name)

    def __str__(self):
        return self.get_display_name()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["title", "unit"], name="unique_note_title"),
            models.UniqueConstraint(fields=["file", "unit"], name="unique_note_file"),
        ]

    def save(self, *args, **kwargs):
        if not self.title:
            # Extract filename without extension and set it as title
            self.title = os.path.splitext(os.path.basename(self.file.name))[0]
        super().save(*args, **kwargs)


class UserRequest(models.Model):
    yourschool = models.CharField(max_length=20, null=True)
    yourcourse = models.CharField(max_length=20, null=True)
    enquiry = models.TextField(blank=True)

    def __str__(self):
        return f"{self.yourschool} - {self.yourcourse}"
