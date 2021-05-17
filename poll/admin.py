from django.contrib import admin
from .models import (
    Question,
    Choice,
)

# Register your models here.

class ChoiceTabular(admin.TabularInline):
    model = Choice
    extra = 4
    max_num = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceTabular, ]
    fieldsets = (
        ('Question', {
            'fields': (
                'question', 
            ),
        }),
    )    


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)