# RoadMk

Веб апликација за следење на состојбата на патната мрежа во Македонија.

## Опис

За овој проект направив апликација која автоматски ги зема дневните извештаи за состојбата на патиштата од официјалната страница на АМСМ (Авто-Мото Сојуз на Македонија) и ги прикажува на попрегледен начин.

Проблемот е што АМСМ ги објавува тие информации само како голем блок текст кој е тежок за читање. Со оваа апликација сакав да ги организирам по важност и да овозможам лесно филтрирање.

Апликацијата работи самостојно — на секои 30 минути автоматски ги зема новите информации, ги зачувува во база и ги брише застарените записи.

## Функционалности

- Автоматско scraping на АМСМ страницата на секои 30 минути
- Класификација на извештаите: RED (затворено), YELLOW (предупредување), GREEN (нормално)
- Филтрирање по статус и категорија
- Автоматско бришење на застарени извештаи
- Статистика во реално време
- REST API со Swagger документација

## Технологии

**Backend:**
- Python 3.10
- FastAPI
- SQLAlchemy (ORM)
- APScheduler (автоматско scraping)
- BeautifulSoup4 (парсирање на HTML)
- psycopg2

**База на податоци:**
- PostgreSQL (во Docker контејнер)
- docker-compose

**Frontend:**
- Vue.js 3 (Composition API)
- Vue Router
- Vite
- Fetch API
- CSS Custom Properties

## Структура на проектот


RoadMk/
├── main.py # FastAPI апликација и scheduler
├── models.py # SQLAlchemy модели
├── database.py # Конекција со базата
├── amsm_scraper.py # Scraper логика
├── scraper_job.py # Scheduler job
├── create_tables.py # Креирање на табели
├── insert_reports.py # Вметнување на податоци
├── docker-compose.yaml # Docker конфигурација
└── roadmk-frontend/ # Vue.js frontend
└── src/
├── api/
│ └── reports.js # API повици
├── views/
│ ├── HomeView.vue # Почетна страница
│ ├── RoadsView.vue # Состојба на патишта
│ ├── AboutView.vue # За нас
│ └── ContactView.vue # Контакт
├── router/
│ └── index.js # Vue Router
└── App.vue # Главен компонент



## API Endpoints

| Метод | Endpoint | Опис |
|---|---|---|
| GET | /reports | Сите извештаи, поддржува филтрирање по severity, category, status_type |
| GET | /reports/{id} | Еден извештај по ID |
| GET | /summary | Статистика — вкупно, RED, YELLOW, GREEN, активни |

Swagger документација: `http://localhost:8001/docs`

## Kako се стартува

### Барања
- Python 3.10+
- Node.js 18+
- Docker Desktop

### Backend

```bash
docker-compose up -d
pip install fastapi uvicorn sqlalchemy psycopg2-binary apscheduler beautifulsoup4 requests
uvicorn main:app --port 8001
```

### Frontend

```bash
cd roadmk-frontend
npm install
npm run dev
```

Апликацијата е достапна на `http://localhost:5173`

## Класификација на извештаи

| Тежина | Клучни зборови | Значење |
|---|---|---|
| RED | затвор, забран, прекин | Целосно затворање |
| YELLOW | девија, градежни, снег, магла | Предупредување |
| GREEN | останато | Нормална состојба |