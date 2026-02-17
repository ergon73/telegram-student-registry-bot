# Telegram Student Registry Bot

Telegram-бот для регистрации студентов с сохранением данных в SQLite.

Бот последовательно запрашивает имя, возраст и класс, валидирует ввод
и сохраняет запись в базу данных. Построен на **aiogram 3** с использованием
FSM (Finite State Machine) для управления пошаговым диалогом.

## Возможности

- Пошаговый диалог с FSM (`StatesGroup` / `FSMContext`)
- Валидация возраста (целое число от 1 до 120)
- Хранение данных в SQLite (`school_data.db`, таблица `students`)
- Автоматическая инициализация базы данных при запуске
- Команда `/cancel` для отмены ввода на любом шаге
- Команда `/help` — справка по командам
- Утилита для просмотра записей в базе

## Стек

- Python 3.10+
- aiogram 3 (Telegram Bot API)
- SQLite (`sqlite3`, стандартная библиотека)
- python-dotenv (загрузка переменных окружения)

## Быстрый старт (Windows 11, PowerShell)

### 1. Клонировать репозиторий

```powershell
git clone https://github.com/<username>/telegram-student-registry-bot.git
cd telegram-student-registry-bot
```

### 2. Создать виртуальное окружение

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Установить зависимости

```powershell
python -m pip install -U pip
pip install -r requirements.txt
```

### 4. Настроить переменные окружения

```powershell
Copy-Item .env.example .env
```

Открой `.env` и задай токен бота:

```text
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 5. Запустить бота

```powershell
python -m bot.main
```

## Использование

1. Открой бота в Telegram.
2. Отправь `/start`.
3. Ответь на вопросы: имя, возраст, класс.
4. Бот подтвердит сохранение и покажет `id` записи.
5. Для отмены на любом шаге отправь `/cancel`.
6. Команда `/help` показывает список команд и краткую справку.

## Схема базы данных

**Таблица:** `students`

| Столбец | Тип | Ограничение |
|---------|-----|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| name | TEXT | NOT NULL |
| age | INTEGER | NOT NULL |
| grade | TEXT | NOT NULL |

## Проверка сохранённых данных

```powershell
python scripts/inspect_db.py
```

## Структура проекта

```text
telegram-student-registry-bot/
├── bot/
│   ├── __init__.py      # пакет
│   ├── main.py          # точка входа, хендлеры
│   ├── states.py        # FSM-состояния
│   └── db.py            # работа с SQLite
├── scripts/
│   └── inspect_db.py    # утилита просмотра БД
├── config.py            # загрузка BOT_TOKEN
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Автор

**Георгий Белянин** (Georgy Belyanin)  
georgy.belyanin@gmail.com

## Лицензия

MIT
