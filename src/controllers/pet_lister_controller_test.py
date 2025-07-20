from src.controllers.pet_lister_controller import PetListerController
from src.models.sqlite.entities.pets import PetsTable


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="Cat", id=4),
            PetsTable(name="Buddy", type="Dog", id=5),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pet",
            "count": 2,
            "attributes": [
                {"name": "Fluffy", "id": 4},
                {"name": "Buddy", "id": 5},
            ],
        }
    }

    assert response == expected_response
