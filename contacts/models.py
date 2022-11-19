from django.db import models

# Create your models here.
from django.db import models

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):
    firstname = models.CharField(verbose_name="Firstname", max_length=100)
    lastname = models.CharField(verbose_name="Lastname", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)

    mobile_phone = models.CharField(verbose_name="Mobile phone", max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Numbers(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="numbers")
    phone = models.CharField(verbose_name="Phone", max_length=100)
