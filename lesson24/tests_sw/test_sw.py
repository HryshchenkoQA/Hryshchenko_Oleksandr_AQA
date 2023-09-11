from lesson24.test_data.people_test_data import test_data


def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == "Luke Skywalker"

# def test_test_multiply_person(people_service):
#     response = people_service.get_people(test_data)
