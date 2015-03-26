from django.contrib import admin
from django.contrib import admin
from user_messages.models import *
from user.models import *
# Register your models here.
admin.site.register(messages)
admin.site.register(User)
