from django.contrib import admin

from guestbooksapp.models import GuestBookRecord


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'status', 'created_at']
    list_filter = ['author', 'status']
    search_fields = ['author']
    fields = ['author', 'text', 'email', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(GuestBookRecord, RecordAdmin)
