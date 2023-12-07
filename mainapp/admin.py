from django.contrib import admin
from mainapp.models import College, School, Department, Course, Unit, UnitTopic, Note


class CollegeAdmin(admin.ModelAdmin):
    search_fields = ['name']


class SchoolAdmin(admin.ModelAdmin):
    list_filter = ['college']
    search_fields = ['name', ]


class DepartmentAdmin(admin.ModelAdmin):
    list_filter = ['school']
    search_fields = ['name', 'school']


class CourseAdmin(admin.ModelAdmin):
    list_filter = ['department']
    search_fields = ['name', 'department', 'year_of_study']


class CourseAdmin(admin.ModelAdmin):
    list_filter = ['department']
    search_fields = ['name', 'department', 'year_of_study']


class UnitAdmin(admin.ModelAdmin):
    list_filter = ['course', 'year_of_study' ,'uploaded_by']
    date_hierarchy = 'uploaded_at'


class UnitTopicAdmin(admin.ModelAdmin):
    list_filter = ['unit', ]
    search_fields = ['name', 'unit']


class UnitTopicAdmin(admin.ModelAdmin):
    list_filter = ['un', ]
    search_fields = ['name', 'unit']


admin.site.register(College, CollegeAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(UnitTopic)
admin.site.register(Note)
