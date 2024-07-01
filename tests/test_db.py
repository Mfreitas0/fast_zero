from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username="marcos", password="senha", email="email@email.com")

    session.add(user)
    session.commit()
    session.scalar(select(User).where(User.email == "email@email.com"))

    assert user.id == 1
