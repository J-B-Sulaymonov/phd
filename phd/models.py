from django.db import models

from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

class Suz_uzgartiruvchilar(models.Model):
    name = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "So'z o'zgartiruvchilar"
        verbose_name_plural = "So'z o'zgartiruvchilar"

class UZB_affiks(models.Model):
    name = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "O'zb affiks"
        verbose_name_plural = "O'zb affiks"

class Shakil_yasovchi_qushimchalar(models.Model):
    name = models.CharField(max_length=1000, default="")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shakil yasovchi qo'shimchalar"
        verbose_name_plural = "Shakil yasovchi qo'shimchalar"

class Suzlar(models.Model):
    name = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "So'zlar"
        verbose_name_plural = "So'zlar"
# class Account(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=1000, default="",  null=True,blank=True, verbose_name='Familiya Ism Sharif')
#     img = models.ImageField(upload_to='images/user/', default="#",verbose_name='Rasm (3x4)')
#     phone = models.CharField(max_length=20, default="", null=True,blank=True, verbose_name='Telefon')
#     Email = models.CharField(max_length=200, default="", null=True,blank=True )
#     id_cart = models.CharField(max_length=200, default="", null=True,blank=True, verbose_name='Id karta')
#     online_status = models.BooleanField(default=False)
#     created_date = models.DateTimeField(auto_now_add=True, max_length=80)
#     updated_date = models.DateTimeField( auto_now = True, max_length=80)
#     def __str__(self):
#         return self.name
