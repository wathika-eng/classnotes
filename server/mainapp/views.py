from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (
    CollegeSerializer,
    SchoolSerializer,
    DepartmentSerializer,
    CourseSerializer,
    UnitSerializer,
    NoteSerializer,
    UserSerializer,
    UserRequestSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics, viewsets
from .models import (
    College,
    School,
    Department,
    Course,
    Unit,
    Note,
    User,
    UserRequest,
)

# no authentication required currently


class CollegeListCreateView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    # permission_classes = [IsAuthenticated]


class CollegeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    # permission_classes = [IsAuthenticated]


class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = [IsAuthenticated]


class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [IsAuthenticated]


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsAuthenticated]


class UnitListCreateView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    # permission_classes = [IsAuthenticated]


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = [IsAuthenticated]


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


# class UnitTopicListCreateView(generics.ListCreateAPIView):
#     queryset = UnitTopic.objects.all()
#     serializer_class = UnitTopicSerializer
#     # permission_classes = [IsAuthenticated]


class SchoolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = [IsAuthenticated]


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [IsAuthenticated]


class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsAuthenticated]


class UnitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    # permission_classes = [IsAuthenticated]


class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = [IsAuthenticated]


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


# class UnitTopicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UnitTopic.objects.all()
#     serializer_class = UnitTopicSerializer
#     # permission_classes = [IsAuthenticated]


class UserRequestListCreateView(generics.ListCreateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer
    # permission_classes = [IsAuthenticated]


class UserRequestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer
    # permission_classes = [IsAuthenticated]


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = [IsAuthenticated]


def error_404_view(request, exception):
    return Response({"error": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
