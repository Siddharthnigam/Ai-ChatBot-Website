from django.contrib import admin

# Register your models here.

from ai.models import Contact
from ai.models import User
from ai.models import TrainingData

admin .site.register(Contact)  # Register the Contact model
admin .site.register(User)
admin .site.register(TrainingData)
