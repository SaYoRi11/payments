from django.contrib import admin
from .models import Card, Invoice, User

admin.site.register([Card, Invoice, User])
