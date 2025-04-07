import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Формирование строки подключения через переменные окружения
db_user = os.environ.get('DATABASE_USER', 'app_user')
db_password = os.environ.get('DATABASE_PASSWORD', 'secret')
db_host = os.environ.get('DATABASE_HOST', 'db')
db_port = os.environ.get('DATABASE_PORT', 5432)
db_name = os.environ.get('DATABASE_NAME', 'app_db')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Импорт моделей и маршрутов
from app import routes, models

# Автоматическое создание таблиц (симуляция миграций)
@app.before_first_request
def create_tables():
    db.create_all()
