from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Idea, Report

admin.site.register(User, UserAdmin)
admin.site.register(Idea)
admin.site.register(Report)
