from .base import DoorLoopTestCase


class TestAccounts(DoorLoopTestCase):

    def setUp(self):
        payload = {
            "name": "Test",
            "active": True,
            "type": "ASSET_OTHER_ASSETS"
        }
        response = self.dl.accounts.create(payload)
        assert isinstance(response, dict)
        assert response.get('id')
        self.account_id = response.get('id')

    def tearDown(self):
        if self.account_id:
            self.dl.accounts.delete(self.account_id)

    def test_list_accounts(self):
        response = self.dl.accounts.list()
        assert isinstance(response, dict)
        assert response['data'][0].get('name')

    def test_create_account(self):
        pass

    def test_retrieve_account(self):
        response = self.dl.accounts.retrieve(self.account_id)
        assert isinstance(response, dict)
        assert response.get('name')

    def test_update_account(self):
        payload = {
            'id': self.account_id,
            'name': 'Test Update',
            'active': False,
            "type": "ASSET_OTHER_ASSETS"
        }
        response = self.dl.accounts.update(self.account_id, payload)
        assert isinstance(response, dict)
        assert response.get('name')
        assert response['name'] == 'Test Update'

    def test_delete_account(self):
        response = self.dl.accounts.delete(self.account_id)
        assert isinstance(response, dict)
        self.account_id = None
