from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username="marcos", password="senha", email="email@email.com"
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "marcos"))

    assert user.id == 1
