from src.doorloop.main import DoorLoop

dl = DoorLoop()


def test_list_users():
    response = dl.users.list()
    assert isinstance(response, dict)
    assert response['data'][0].get('id')


def test_retrieve_user():
    response = dl.users.list()
    assert isinstance(response, dict)
    user_id = response['data'][0].get('id')
    assert user_id
    user_rep = dl.users.retrieve(user_id)
    assert user_rep.get('id')
    assert isinstance(user_rep.get('bankAccounts'), list)


def test_get_current_user():
    response = dl.users.get_current()
    assert isinstance(response, dict)
    assert response.get('id')
    assert isinstance(response.get('bankAccounts'), list)
