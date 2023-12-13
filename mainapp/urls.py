from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import note_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.my_login, name="login"),
    path("logout", views.my_logout, name="mylogout"),
    path("", views.dashboard, name="dashboard"),
    path("dash", views.dashboard, name="dashboard"),
    path('send-reset-email/', views.send_password_reset_email, name='send_password_reset_email'),
    path("create_record", views.create_record, name="create_record"),
    path("unit", views.create_unit, name="unit"),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('get_colleges/', note_views.get_colleges, name="get_colleges"),
    path('get_schools/', note_views.get_schools, name='get_schools'),
    path('get_departments/', note_views.get_departments, name='get_departments'),
    path('get_courses/', note_views.get_courses, name='get_courses'),
    path('get_units/', note_views.get_units, name='get_units'),
    path('submit_notes/', note_views.submit_notes, name='submit_notes'),
    path('unit_topic_details/<int:unit_topic_id>/', note_views.unit_topic_details, name='unit_topic_details'),
    path('unit_details/<int:unit_id>/', note_views.unit_details, name="unit_details"),
    path('course_details/<int:course_id>/', note_views.course_details, name="course_details"),
    path('department_details/<int:department_id>/', note_views.department_details, name="department_details"),
    path('school_details/<int:school_id>/', note_views.school_details, name="school_details"),
    path('college_details/<int:college_id>/', note_views.college_details, name="college_details"),
    path('mpesa', views.mpesa, name="mpesa"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
