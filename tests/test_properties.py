from src.doorloop.main import DoorLoop


dl = DoorLoop()


def test_list_properties():
    response = dl.properties.list()
    assert isinstance(response, dict)
    assert response['data'][0].get('address')


def test_list_properties_filter_text():
    # Filter by Property Name
    pass


def test_list_properties_filter_group():
    # Filter by Portfolio
    pass


def test_list_properties_filter_class():
    # Filter by Property Type
    pass


def test_list_properties_filter_owner():
    # Filter by Property Owner
    pass


def test_retrieve_property():
    response = dl.properties.list(query_params={'page_size': 100})
    assert isinstance(response, dict)
    property_id = response['data'][0].get('id')
    property_rep = dl.properties.retrieve(property_id)
    assert isinstance(property_rep, dict)
    assert property_rep.get('address')

