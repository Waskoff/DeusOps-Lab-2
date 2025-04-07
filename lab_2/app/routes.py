from app import app, db
from flask import jsonify
from app.models import Item

# Маршрут для получения всех элементов
@app.route('/')
def index():
    items = Item.query.all()
    data = [{'id': item.id, 'name': item.name} for item in items]
    return jsonify(data)

# Маршрут для добавления элемента через URL-параметр
@app.route('/add/<name>')
def add_item(name):
    new_item = Item(name=name)
    db.session.add(new_item)
    db.session.commit()
    return f"Added {name}!"
