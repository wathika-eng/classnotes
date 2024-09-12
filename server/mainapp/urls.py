from .views import (
    APITest,
    SchoolListCreateView,
    CollegeListCreateView,
    CollegeRetrieveUpdateDestroyView,
    DepartmentListCreateView,
    CourseListCreateView,
    UnitListCreateView,
    NoteListCreateView,
    UserListCreateView,
    UserDetail,
    # UnitTopicListCreateView,
    LogoutView,
    SignUpView,
    LoginView,
    UserRequestListCreateView,
    SchoolRetrieveUpdateDestroyView,
    DepartmentRetrieveUpdateDestroyView,
    CourseRetrieveUpdateDestroyView,
    UnitRetrieveUpdateDestroyView,
    NoteRetrieveUpdateDestroyView,
    UserRetrieveUpdateDestroyView,
    # UnitTopicRetrieveUpdateDestroyView,
    UserRequestRetrieveUpdateDestroyView,
)
from django.urls import path

urlpatterns = [
    path("test", APITest, name="api-root"),
    path("auth/signup", SignUpView.as_view(), name="signup"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("me", UserDetail.as_view(), name="me"),
    path("colleges", CollegeListCreateView.as_view(), name="college-list-create"),
    path(
        "colleges<int:pk>",
        CollegeRetrieveUpdateDestroyView.as_view(),
        name="college-rud",
    ),
    path("schools", SchoolListCreateView.as_view(), name="school-list-create"),
    path(
        "departments",
        DepartmentListCreateView.as_view(),
        name="department-list-create",
    ),
    path("courses", CourseListCreateView.as_view(), name="course-list-create"),
    path("units", UnitListCreateView.as_view(), name="unit-list-create"),
    path("notes", NoteListCreateView.as_view(), name="note-list-create"),
    path("users", UserListCreateView.as_view(), name="user-list-create"),
    # path(
    #     "unit-topics", UnitTopicListCreateView.as_view(), name="unit-topic-list-create"
    # ),
    path(
        "user-requests",
        UserRequestListCreateView.as_view(),
        name="user-request-list-create",
    ),
    path(
        "schools<int:pk>",
        SchoolRetrieveUpdateDestroyView.as_view(),
        name="school-rud",
    ),
    path(
        "departments<int:pk>",
        DepartmentRetrieveUpdateDestroyView.as_view(),
        name="department-rud",
    ),
    path(
        "courses<int:pk>",
        CourseRetrieveUpdateDestroyView.as_view(),
        name="course-rud",
    ),
    path("units<int:pk>", UnitRetrieveUpdateDestroyView.as_view(), name="unit-rud"),
    path("notes<int:pk>", NoteRetrieveUpdateDestroyView.as_view(), name="note-rud"),
    path("users<int:pk>", UserRetrieveUpdateDestroyView.as_view(), name="user-rud"),
    # path(
    #     "unit-topics<int:pk>",
    #     UnitTopicRetrieveUpdateDestroyView.as_view(),
    #     name="unit-topic-rud",
    # ),
    path(
        "user-requests<int:pk>",
        UserRequestRetrieveUpdateDestroyView.as_view(),
        name="user-request-rud",
    ),
]
