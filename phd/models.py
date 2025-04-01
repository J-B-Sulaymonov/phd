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
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "So'zlar"
        verbose_name_plural = "So'zlar"

class AtoqliSuzlar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Atoqli so'zlar"
        verbose_name_plural = "Atoqli so'zlar"

class Raqamlar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Raqamlar"
        verbose_name_plural = "Raqamlar"

class BuyruqSozlar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Buyruq so'zlar"
        verbose_name_plural = "Buyruq so'zlar"

class ModalSozlar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Modal so'zlar"
        verbose_name_plural = "Modal so'zlar"

class SoroqSozlar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "So'roq so'zlar"
        verbose_name_plural = "So'roq so'zlar"

class SonlarNomi(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sonlar nomi"
        verbose_name_plural = "Sonlar nomi"

class KomakchiSozlar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ko'makchi so'zlar"
        verbose_name_plural = "Ko'makchi so'zlar"

class BoglovchiSozlar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bog'lovchi so'zlar"
        verbose_name_plural = "Bog'lovchi so'zlar"

class UndoviSozlar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Undov so'zlar"
        verbose_name_plural = "Undov so'zlar"

class YondoshFellar(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name="Nomi")
    muqobili = models.CharField(max_length=1000, default="", blank=True, null=True, verbose_name="Muqobillari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yondosh fellar"
        verbose_name_plural = "Yondosh fellar"