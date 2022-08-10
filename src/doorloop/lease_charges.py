from .base import DoorLoopBase


class DoorLoopLeaseCharge(DoorLoopBase):
    endpoint_base = '/lease-charges'

    def list(self, **kwargs):
        '''
        List all Lease Charges
        https://api.doorloop.com/reference/get-lease-charges
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Lease Charge
        https://api.doorloop.com/reference/post-lease-charge
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, lease_charge_id, **kwargs):
        '''
        Retrieve a Lease Charge
        https://api.doorloop.com/reference/get-lease-charge
        '''
        response = self.connector.get(f'{self.endpoint_base}/{lease_charge_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, lease_charge_id, data, **kwargs):
        '''
        Update a Lease Charge
        https://api.doorloop.com/reference/put-lease-charge
        '''
        response = self.connector.put(f'{self.endpoint_base}/{lease_charge_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, lease_charge_id, **kwargs):
        '''
        Delete a Lease Charge
        https://api.doorloop.com/reference/delete-lease-charge
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{lease_charge_id}', **kwargs)
        return self.validator(response).validate()