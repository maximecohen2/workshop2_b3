from django.contrib import admin

# Register your models here.
from project.models import Project, Team

admin.site.register(Project)
admin.site.register(Team)
