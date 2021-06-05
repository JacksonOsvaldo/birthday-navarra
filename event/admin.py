from django.contrib import admin
from .models import UserEvent

# registrando app no admin
admin.site.register(UserEvent)
