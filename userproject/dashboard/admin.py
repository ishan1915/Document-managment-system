from django.contrib import admin
from .models import UserDetail,Task,DocumentVersion,Message

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("user","firstname","lastname","contact","address")
admin.site.register(UserDetail,MemberAdmin)


admin.site.register(Task)
admin.site.register(DocumentVersion)
admin.site.register(Message)
