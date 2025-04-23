# Auth-OOP API

## Stack
- FastAPI + SQLAlchemy + Alembic
- PostgreSQL (Docker)
- Redis (для хранения Refresh Token)
- Stripe API для оплаты
- RabbitMQ для отправки заказов на кухню
- CI/CD (GitHub Actions)
- Nginx (балансировка + защита)
- Swagger с авторизацией через JWT
- Docker Compose для запуска всех сервисов

## API Endpoints

### Auth
- `POST /register` - регистрация
- `POST /login` - логин
- `POST /logout` - выход (по access/refresh token)

### Orders (WIP)
- `POST /orders` - создать заказ
- `GET /orders/{id}` - получить заказ

## Хранение токенов
- Access Token → localStorage
- Refresh Token → Redis

## Планы
- `items`, `orders`, корзина на фронте в `localStorage`
- Stripe: оплата заказов
- RabbitMQ: отправка заказов на кухню
- CI/CD: автодеплой
- Swagger авторизация по JWT

## Запуск

```
docker-compose up --build
```
