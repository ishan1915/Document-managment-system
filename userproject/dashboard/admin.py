from django.contrib import admin
from .models import UserDetail

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("user","firstname","lastname","contact","address")
admin.site.register(UserDetail,MemberAdmin)


 