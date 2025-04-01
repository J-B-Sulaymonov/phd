from django.contrib import admin
from phd.models import Suz_uzgartiruvchilar,UZB_affiks,Shakil_yasovchi_qushimchalar,Suzlar,AtoqliSuzlar,Raqamlar,BuyruqSozlar,ModalSozlar,SoroqSozlar,SonlarNomi,KomakchiSozlar,BoglovchiSozlar,UndoviSozlar,YondoshFellar

class SuzlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class AtoqliSuzlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class BoglovchiSozlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class BuyruqSozlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class KomakchiSozlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class ModalSozlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class SoroqSozlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class SonlarNomiAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class UndoviSozlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]
class YondoshFellarAdmin(admin.ModelAdmin):
    list_display = ('name', 'muqobili',)
    search_fields = ['name',]


admin.site.register(Suz_uzgartiruvchilar)
admin.site.register(UZB_affiks)
admin.site.register(Shakil_yasovchi_qushimchalar)
admin.site.register(Suzlar,SuzlarAdmin)
admin.site.register(AtoqliSuzlar, AtoqliSuzlarAdmin)
admin.site.register(Raqamlar)
admin.site.register(BuyruqSozlar, BuyruqSozlarAdmin)
admin.site.register(ModalSozlar, ModalSozlarAdmin)
admin.site.register(SoroqSozlar, SoroqSozlarAdmin)
admin.site.register(SonlarNomi, SonlarNomiAdmin)
admin.site.register(KomakchiSozlar, KomakchiSozlarAdmin)
admin.site.register(BoglovchiSozlar, BoglovchiSozlarAdmin)
admin.site.register(UndoviSozlar, UndoviSozlarAdmin)
admin.site.register(YondoshFellar, YondoshFellarAdmin)
