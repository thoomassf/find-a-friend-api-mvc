import pytest

from src.models.sqlite.settings.connection import db_connection_handler

from .people_repository import PesopleRepository
from .pets_repository import PetsRepository

# db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interacao com o banco")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)


@pytest.mark.skip(reason="interacao com o banco")
def test_delete_pet():
    name = "shrek"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)


@pytest.mark.skip(reason="interacao com o banco")
def test_insert_person():
    first_name = "test name"
    last_name = "test last"
    age = 77
    pet_id = 2

    repo = PesopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)


@pytest.mark.skip(reason="interacao com o banco")
def test_get_person():
    person_id = 1

    repo = PesopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
