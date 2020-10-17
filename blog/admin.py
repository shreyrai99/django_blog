from django.contrib import admin
from .models import Post, Question, Choice

# Register your models here.
admin.site.register(Post)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)