from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    is_employee = models.BooleanField(default=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        db_table = 'employee'

# Create your models here.
