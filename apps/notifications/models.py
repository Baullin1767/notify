from django.db import models
from .choices import Channel, Status

class UserContact(models.Model):
    user_id = models.UUIDField()  # внешний user_id
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    telegram_chat_id = models.CharField(max_length=64, null=True, blank=True)
    preferred_order = models.JSONField(default=list)  # ["email","telegram","sms"]

    def __str__(self):
        return f"{self.user_id}"

class Template(models.Model):
    code = models.CharField(max_length=64, unique=True)
    locale = models.CharField(max_length=8, default="en")
    subject = models.CharField(max_length=256, blank=True, default="")
    body_text = models.TextField()
    body_html = models.TextField(blank=True, default="")
    channel_overrides = models.JSONField(default=dict)  # { "sms": "{title}: {code}" ... }
    category = models.CharField(max_length=64, default="general")
    active = models.BooleanField(default=True)
    version = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} ({self.locale})"

class Notification(models.Model):
    idempotency_key = models.CharField(max_length=64, db_index=True, null=True, blank=True)
    user = models.ForeignKey(UserContact, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, null=True, blank=True, on_delete=models.SET_NULL)
    payload = models.JSONField(default=dict)          # данные для рендера
    channel_order = models.JSONField(default=list)    # если пусто → возьмем из user.preferred_order
    status = models.CharField(max_length=16, choices=Status, default="queued")
    final_channel = models.CharField(max_length=16, choices=Channel, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification #{self.pk} -> {self.user_id if hasattr(self, 'user_id') else self.user}"

class DeliveryAttempt(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name="attempts")
    channel = models.CharField(max_length=16, choices=Channel)
    external_id = models.CharField(max_length=128, null=True, blank=True)  # id сообщения у провайдера
    status = models.CharField(max_length=16, choices=Status, default="queued")
    error = models.TextField(blank=True, default="")
    meta = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserPreferences(models.Model):
    user = models.OneToOneField(UserContact, on_delete=models.CASCADE)
    subscriptions = models.JSONField(default=dict)   # {"marketing": false, "system": true}
    quiet_hours = models.JSONField(default=dict)     # {"start":"22:00","end":"08:00","tz":"Europe/Belgrade"}
    channel_enabled = models.JSONField(default=dict) # {"email": true, "sms": true, "telegram": true}
