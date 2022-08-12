from src.doorloop.main import DoorLoop


dl = DoorLoop()


def test_list_leases():
    response = dl.leases.list()
    assert isinstance(response, dict)
    assert response['data'][0].get('name')


def test_retrieve_lease():
    response = dl.leases.list()
    assert isinstance(response, dict)
    lease_id = response['data'][0].get('id')
    assert lease_id
    lease_rep = dl.leases.retrieve(lease_id)
    assert isinstance(lease_rep, dict)
    assert lease_rep.get('name')


def test_move_in_tenant():
    pass


def test_move_out_tenant():
    pass


def test_list_lease_tenants():
    response = dl.leases.list()
    assert isinstance(response, dict)
    lease_id = response['data'][0].get('id')
    assert lease_id
    lease_resp = dl.leases.list_lease_tenants(lease_id)
    assert isinstance(lease_resp, dict)
    assert response['data'][0].get('name')
