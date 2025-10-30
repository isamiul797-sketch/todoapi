from django.contrib import admin
from tasks.models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','description','completed','created_at']
