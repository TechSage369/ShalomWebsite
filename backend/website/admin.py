from django.contrib import admin
from .models import (
    FeedbackModel,
    FeeStructure,
)


class FeedbackModelAdmin(admin.ModelAdmin):
    readonly_fields = ['fullname', 'feedback']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If editing an existing object
            return self.readonly_fields  # Return the fields as read-only
        return ()  # Otherwise, return an empty tuple to allow modifications

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.site_header = "Shalom English Academy Administration"
admin.site.index_title = "Welcome to Shalom English School Administration"
admin.site.site_title = "Shalom English Academy Administration"

admin.site.register(FeedbackModel, FeedbackModelAdmin)
admin.site.register(FeeStructure)
