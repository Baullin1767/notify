# Простые tuple-choices — совместимо с любой версией Django

Channel = (
    ("email", "Email"),
    ("sms", "SMS"),
    ("telegram", "Telegram"),
)

Status = (
    ("queued", "Queued"),
    ("sent", "Sent"),
    ("failed", "Failed"),
)
