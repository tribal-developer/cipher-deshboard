from django.contrib import admin
from .models import CipherRecord, UserVerification
admin.site.site_header = "Cipher Management System"
admin.site.site_title = "CMS Admin"
admin.site.index_title = "Administration"


@admin.register(CipherRecord)
class CipherRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'agent_name',
        'section',
        'created_by',
        'uploaded_date'
    )

    search_fields = (
        'name',
        'agent_name',
        'section'
    )

    list_filter = (
        'section',
        'uploaded_date'
    )


@admin.register(UserVerification)
class UserVerificationAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id',
        'designation',
        'section',
    )

    search_fields = (
        'employee_id',
        'designation',
        'section'
    )