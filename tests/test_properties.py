from src.doorloop.main import DoorLoop


dl = DoorLoop()


def test_list_properties():
    response = dl.properties.list()
    assert isinstance(response, dict)
    assert response['data'][0].get('address')


def test_retrieve_property():
    response = dl.properties.list()
    assert isinstance(response, dict)
    property_id = response['data'][0].get('id')
    property_rep = dl.properties.retrieve(property_id)
    assert isinstance(property_rep, dict)
    assert response['data'][0].get('address')

