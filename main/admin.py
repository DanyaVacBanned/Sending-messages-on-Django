from django.contrib import admin
from .models import users, messages
# Register your models here.
admin.site.register(users)
admin.site.register(messages)