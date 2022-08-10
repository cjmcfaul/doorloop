from .base import DoorLoopBase


class DoorLoopVendorCredit(DoorLoopBase):
    endpoint_base = '/vendor-credits'
    
    def list(self, **kwargs):
        '''
        List all Vendor Credits
        https://api.doorloop.com/reference/get-vendor-credits
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Vendor Credit
        https://api.doorloop.com/reference/post-vendor-credit
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, vendor_credit_id, **kwargs):
        '''
        Retrieve a Vendor Credit
        https://api.doorloop.com/reference/get-vendor-credit
        '''
        response = self.connector.get(f'{self.endpoint_base}/{vendor_credit_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, vendor_credit_id, data, **kwargs):
        '''
        Update a Vendor Credit
        https://api.doorloop.com/reference/put-vendor-credit
        '''
        response = self.connector.put(f'{self.endpoint_base}/{vendor_credit_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, vendor_credit_id, **kwargs):
        '''
        Delete a Vendor Credit
        https://api.doorloop.com/reference/delete-vendor-credit
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{vendor_credit_id}', **kwargs)
        return self.validator(response).validate()
