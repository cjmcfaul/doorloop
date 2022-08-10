from .base import DoorLoopBase


class DoorLoopLeaseReturnedPayments(DoorLoopBase):
    endpoint_base = '/lease-reversed-payments'

    def list(self, **kwargs):
        '''
        List all Lease Returned Payments
        https://api.doorloop.com/reference/get-lease-reversed-payments
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Lease Returned Payment
        https://api.doorloop.com/reference/post-lease-reversed-payments
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, lease_returned_payment_id, **kwargs):
        '''
        Retrieve a Lease Returned Payment
        https://api.doorloop.com/reference/get-lease-reversed-payment
        '''
        response = self.connector.get(f'{self.endpoint_base}/{lease_returned_payment_id}', **kwargs)
        return self.validator(response).validate()

    def delete(self, lease_returned_payment_id, **kwargs):
        '''
        Delete a Lease Returned Payment
        https://api.doorloop.com/reference/delete-lease-reversed-payment
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{lease_returned_payment_id}', **kwargs)
        return self.validator(response).validate()
