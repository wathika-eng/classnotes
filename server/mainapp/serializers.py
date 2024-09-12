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
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password", "role")
        read_only_fields = ("role",)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


# class UnitTopicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UnitTopic
#         fields = "__all__"


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = "__all__"
