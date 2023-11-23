from src.user.user import User
from src.food.recipe import Recipe
from src.food.ingredient import Ingredient


def test_user_init():
    user = User(
        username="maciek",
        password="haslo123",
        email="maciek123@gmail.com",
        premium=False,
        allergies=["peanuts", "milk"],
        vegetarian=True
    )
    assert user.username == "maciek"
    assert user.password == "haslo123"
    assert user.email == "maciek123@gmail.com"
    assert user.premium is False
    assert user.allergies == ["peanuts", "milk"]
    assert user.vegetarian is True


def test_user_allergies():
    user = User(
        username="maciek",
        password="haslo123",
        email="maciek123@gmail.com",
        premium=False,
        allergies=["peanuts"],
        vegetarian=False
    )
    assert user.is_allergic_to("peanuts") is True
    assert user.is_allergic_to("milk") is False

def test_pass():
    pass
