from django.contrib import admin
# Requirements: Seven imported classes (Course, Lesson, Instructor, Learner, Question, Choice, Submission)
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Implementation of ChoiceInline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# Implementation of QuestionInline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

# Implementation of QuestionAdmin with required list_display attributes
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    inlines = [ChoiceInline]

# Implementation of LessonAdmin with required list_display attributes
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

# Registering models according to requirements
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Lesson, LessonAdmin)
