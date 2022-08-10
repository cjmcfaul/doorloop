import unittest

from src.doorloop.main import DoorLoop


dl = DoorLoop()


class TestAccounts(unittest.TestCase):

    def setUp(self):
        payload = {
            "name": "Test 2",
            "active": True,
            "type": "ASSET_OTHER_ASSETS"
        }
        response = dl.accounts.create(payload)
        self.setup_account_id = response.get('id')
        self.created_account_id = None

    def tearDown(self):
        if self.created_account_id:
            dl.accounts.delete(self.created_account_id)

        if self.setup_account_id:
            dl.accounts.delete(self.setup_account_id)

    def test_list_accounts(self):
        response = dl.accounts.list()
        assert isinstance(response, dict)
        assert response['data'][0].get('name')

    def test_create_account(self):
        payload = {
            "name": "Test",
            "active": True,
            "type": "ASSET_OTHER_ASSETS"
        }
        response = dl.accounts.create(payload)
        assert isinstance(response, dict)
        assert response.get('id')
        self.created_account_id = response['id']

    def test_retrieve_account(self):
        response = dl.accounts.retrieve(self.setup_account_id)
        assert isinstance(response, dict)
        assert response.get('name')

    def test_update_account(self):
        payload = {
            'id': self.setup_account_id,
            'name': 'Test Update',
            'active': False,
            "type": "ASSET_OTHER_ASSETS"
        }
        response = dl.accounts.update(self.setup_account_id, payload)
        assert isinstance(response, dict)
        assert response.get('name')
        assert response['name'] == 'Test Update'

    def test_delete_account(self):
        response = dl.accounts.delete(self.setup_account_id)
        assert isinstance(response, dict)
        self.setup_account_id = None
