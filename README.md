# Notify - Django Notifications Service

Cервер для хранения и управления уведомлениями.  
Проект построен на **Django + PostgreSQL** и включает модели для пользователей, шаблонов уведомлений, отправок и предпочтений.
---

## Технологии

- Python 3.11  
- Django 3.2 (LTS)  
- PostgreSQL 15 (через Docker)  

---

## Структура проекта

```
notify/
├─ docker-compose.yml         # запуск сервисов
├─ Dockerfile                 # сборка образа web-приложения
├─ requirements.txt           # зависимости Python
├─ manage.py
├─ notify/                    # пакет проекта
│  ├─ settings_docker_dev.py  # настройки для docker-compose
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ asgi.py
└─ apps/
   └─ notifications/          # приложение уведомлений
      ├─ models.py
      ├─ choices.py
      ├─ admin.py
      ├─ apps.py
      └─ migrations/
```

---

## Запуск проекта

### 1. Клонирование и переход в папку проекта
```bash
git clone <репозиторий>
cd notify
```

### 2. Построить контейнеры и запустить
```bash
docker compose up --build -d
```

Это запустит:
- `db` - PostgreSQL 15  
- `web` - Django-приложение  

### 3. Применить миграции
```bash
docker compose exec web python manage.py makemigrations --settings=notify.settings_docker_dev
docker compose exec web python manage.py migrate --settings=notify.settings_docker_dev
```

### 4. Создать суперпользователя
```bash
docker compose exec web python manage.py createsuperuser --settings=notify.settings_docker_dev
```

### 5. Открыть в браузере
Админка доступна по адресу:  
[http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Основные модели

- **UserContact** - контакты пользователя (email, телефон, telegram).  
- **Template** - шаблоны сообщений с текстом, html и каналами.  
- **Notification** - уведомление, связанное с пользователем и шаблоном.  
- **DeliveryAttempt** - попытки доставки (например, SMS/email).  
- **UserPreferences** - предпочтения: подписки, тихие часы, доступные каналы.  

---
