from .base import DoorLoopBase


class DoorLoopLeasePayment(DoorLoopBase):
    endpoint_base = '/lease-payments'

    def list(self, **kwargs):
        '''
        List all Lease Payments
        https://api.doorloop.com/reference/get-lease-payments
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Lease Payment
        https://api.doorloop.com/reference/post-lease-payment
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, lease_payment_id, **kwargs):
        '''
        Retrieve a Lease Payment
        https://api.doorloop.com/reference/get-lease-payment
        '''
        response = self.connector.get(f'{self.endpoint_base}/{lease_payment_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, lease_payment_id, data, **kwargs):
        '''
        Update a Lease Payment
        https://api.doorloop.com/reference/put-lease-payment
        '''
        response = self.connector.put(f'{self.endpoint_base}/{lease_payment_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, lease_payment_id, **kwargs):
        '''
        Delete a Lease Payment
        https://api.doorloop.com/reference/delete-lease-payment
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{lease_payment_id}', **kwargs)
        return self.validator(response).validate()
