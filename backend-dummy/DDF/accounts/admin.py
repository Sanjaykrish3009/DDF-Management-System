from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser,FacultyUser,CommitteeUser,HodUser,FundRequest, Transaction

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FacultyUser)
admin.site.register(CommitteeUser)
admin.site.register(HodUser)
admin.site.register(FundRequest)
admin.site.register(Transaction)
