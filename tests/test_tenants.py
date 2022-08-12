from .base import DoorLoopTestCase


class TestTenants(DoorLoopTestCase):

    def setUp(self):
        payload = {
            "firstName": "John",
            "lastName": "Smith",
        }
        response = self.dl.tenants.create_prospect(payload)
        assert isinstance(response, dict)
        assert response.get('id')
        self.tenant_id = response.get('id')

    def tearDown(self):
        if self.tenant_id:
            self.dl.tenants.delete(self.tenant_id)

    def test_retrieve(self):
        response = self.dl.tenants.retrieve(self.tenant_id)
        assert isinstance(response, dict)
        assert response.get('name')

    def test_update(self):
        payload = {
            "id": self.tenant_id,
            "firstName": "Jane",
            "lastName": "Doe",
        }
        response = self.dl.tenants.update(self.tenant_id, payload)
        assert isinstance(response, dict)

    def test_delete(self):
        response = self.dl.tenants.delete(self.tenant_id)
        assert isinstance(response, dict)
        self.tenant_id = None

    def test_list(self):
        response = self.dl.tenants.list()
        assert isinstance(response, dict)
        assert response['data'][0].get('name')

    def test_create_prospect(self):
        pass
