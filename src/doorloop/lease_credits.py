from .base import DoorLoopBase


class DoorLoopLeaseCredit(DoorLoopBase):
    endpoint_base = '/lease-credits'

    def list(self, **kwargs):
        '''
        List all Lease Credits
        https://api.doorloop.com/reference/get-lease-credits
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Lease Credit
        https://api.doorloop.com/reference/post-lease-credit
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, lease_credit_id, **kwargs):
        '''
        Retrieve a Lease Credit
        https://api.doorloop.com/reference/get-lease-credit
        '''
        response = self.connector.get(f'{self.endpoint_base}/{lease_credit_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, lease_credit_id, data, **kwargs):
        '''
        Update a Lease Credit
        https://api.doorloop.com/reference/put-lease-credit
        '''
        response = self.connector.put(f'{self.endpoint_base}/{lease_credit_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, lease_credit_id, **kwargs):
        '''
        Delete a Lease Credit
        https://api.doorloop.com/reference/delete-lease-credits-leasecreditid
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{lease_credit_id}', **kwargs)
        return self.validator(response).validate()
