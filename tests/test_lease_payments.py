from .base import DoorLoopTestCase

from datetime import date


class TestLeasePayments(DoorLoopTestCase):
    new_lease_payment_id = None
    deposit_account_id = None

    def setUp(self):
        lease_resp = self.dl.leases.list()
        self.lease_id = lease_resp['data'][0]['id']
        account_resp = self.dl.accounts.list()
        for account in account_resp['data']:
            if account['type'] == "ASSET_BANK":
                self.deposit_account_id = account['id']
                break

    def tearDown(self):
        if self.new_lease_payment_id:
            self.dl.lease_payments.delete(self.new_lease_payment_id)

    def create_testing_lease_payment(self):
        payload = {
            'reference': '1001',
            'amountReceived': 100.00,
            'paymentMethod': 'CASH',
            'lease': self.lease_id,
            'depositToAccount': self.deposit_account_id,
            'autoApplyPaymentOnCharges': True,
            'date': date.today().isoformat(),
        }
        response = self.dl.lease_payments.create(payload)
        print(response.data)
        self.new_lease_payment_id = response['id']
        return response

    def test_list_lease_payments(self):
        response = self.dl.lease_payments.list()
        assert isinstance(response, dict)
        assert response['data'][0].get('reference')

    def test_create_lease_payment(self):
        response = self.create_testing_lease_payment()
        assert isinstance(response, dict)
        assert response['reference']

    def test_retrieve_lease_payment(self):
        if not self.new_lease_payment_id:
            lease_payments_rep = self.dl.lease_payments.list()
            lease_payment_id = lease_payments_rep['data'][0]['id']
        else:
            lease_payment_id = self.new_lease_payment_id
        response = self.dl.lease_payments.retrieve(lease_payment_id)
        assert isinstance(response, dict)
        assert response['reference']

    def test_update_lease_payment(self):
        if not self.new_lease_payment_id:
            self.create_testing_lease_payment()
        response = self.dl.lease_payments.update(
            self.new_lease_payment_id,
            data={
                'amountReceived': 200.00,
                'lease': self.lease_id,
                'depositToAccount': self.deposit_account_id,
            }
        )
        assert isinstance(response, dict)
        assert response['reference']
        assert response['amountReceived'] is 200.00

    def test_delete_lease_payment(self):
        if not self.new_lease_payment_id:
            self.create_testing_lease_payment()
        response = self.dl.lease_payments.delete(
            self.new_lease_payment_id
        )
        assert response['reference']
        self.new_lease_payment_id = None
