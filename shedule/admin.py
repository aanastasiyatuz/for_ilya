from django.contrib import admin
from .models import *

class CourseInline(admin.TabularInline):
    model = Course

class ProfessorAdmin(admin.ModelAdmin):
    inlines = [CourseInline]

class ClassAdmin(admin.ModelAdmin):
    readonly_fields = ['professor']

    def save_model(self, request, obj, form, change):
        obj.professor = obj.course.professor
        obj.save()

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Room)
admin.site.register(Group)
admin.site.register(Class, ClassAdmin)
