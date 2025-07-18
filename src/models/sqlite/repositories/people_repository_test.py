from unittest import mock

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],
                ),
                (
                    [mock.call.query(PeopleTable)],
                    [
                        PeopleTable(
                            first_name="test name",
                            last_name="test last",
                            age=25,
                            pet_id=1,
                        ),
                    ],
                ),
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# def test_get_person():
#     person_id = 1
#     mock_connection = MockConnection()
#     repo = PeopleRepository(mock_connection)
#     response = repo.get_person(person_id)

#     mock_connection.session.query.assert_called_once_with(PeopleTable)
#     # mock_connection.session.outerjoin.assert_called_once()
#     mock_connection.session.filter.assert_called_once_with(PeopleTable.id == person_id)

# assert person.first_name[0] == "test name"


# def test_insert_people():
#     mock_connection = MockConnection()
#     repo = PeopleRepository(mock_connection)
#     repo.insert_person("test name", "test last", 25, 1)
