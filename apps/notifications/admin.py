from django.contrib import admin
from .models import UserContact, Template, Notification, DeliveryAttempt, UserPreferences

@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "email", "phone", "telegram_chat_id")
    search_fields = ("user_id", "email", "phone", "telegram_chat_id")

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "locale", "category", "active", "version", "updated_at")
    search_fields = ("code", "category")
    list_filter = ("active", "locale", "category")

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "template", "status", "final_channel", "created_at")
    list_filter = ("status", "final_channel", "created_at")
    search_fields = ("idempotency_key",)

@admin.register(DeliveryAttempt)
class DeliveryAttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "notification", "channel", "status", "external_id", "created_at", "updated_at")
    list_filter = ("channel", "status")

@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
