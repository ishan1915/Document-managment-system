from django.contrib import admin
from .models import UserDetail,Item

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("user","firstname","lastname","contact","address")
admin.site.register(UserDetail,MemberAdmin)


class MemberAdmin2(admin.ModelAdmin):
    list_display = ("user","name","price","description")
admin.site.register(Item,MemberAdmin2)
