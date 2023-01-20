from src.doorloop.main import DoorLoop


dl = DoorLoop()


def test_list_units():
    response = dl.units.list()
    assert isinstance(response, dict)
    assert response['data'][0].get('address')


def test_list_units_filter_group():
    # Filter by Portfolio
    pass


def test_list_units_filter_property():
    # Filter by Property
    pass


def test_list_units_filter_owner():
    # Filter by Owner
    pass


def test_list_units_filter_text():
    # Filter by Unit Name
    pass


def test_retrieve_unit():
    response = dl.units.list()
    assert isinstance(response, dict)
    unit_id = response['data'][0].get('id')
    unit_rep = dl.units.retrieve(unit_id)
    assert isinstance(unit_rep, dict)
    assert response['data'][0].get('address')