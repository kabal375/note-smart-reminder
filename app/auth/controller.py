from app import db
from app.auth.models import User


def register_user(username, password):
    # Проверка уникальности логина
    if User.query.filter_by(username=username).first() is not None:
        return {'status': 'error', 'message': 'Username already exists'}

    # Создание нового пользователя
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return {'status': 'success', 'message': 'User registered successfully'}