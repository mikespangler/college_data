from django.contrib import admin
from .models import Student, TestScore

admin.site.register(Student)
admin.site.register(TestScore)

class TestScoreInline(admin.StackedInline):
    model = TestScore

class StudentAdmin(admin.ModelAdmin):
    inlines = [
        TestScoreInline,
    ]
    
