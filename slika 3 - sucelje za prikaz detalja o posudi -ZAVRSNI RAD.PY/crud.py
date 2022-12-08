import random

from database import User

def get_all_users(session):
    return session.query(User).all()


def get_only_active_users(session):
    return session.query(User).filter(User.active).all()


def get_by_pin(session, pin):
    return session.query(User).filter(User.pin == pin, User.active).one_or_none()


def get_by_id(session, user_id):
    return session.query(User).get(user_id)





 