from .base import DoorLoopBase


class DoorLoopVendor(DoorLoopBase):
    endpoint_base = '/vendors'

    def list(self, **kwargs):
        '''
        List all Vendors
        https://api.doorloop.com/reference/get-vendors
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Vendor
        https://api.doorloop.com/reference/post-vendor
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, vendor_id, **kwargs):
        '''
        Retrieve a Vendor
        https://api.doorloop.com/reference/get-vendor
        '''
        response = self.connector.get(f'{self.endpoint_base}/{vendor_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, vendor_id, data, **kwargs):
        '''
        Update a Vendor
        https://api.doorloop.com/reference/put-vendor
        '''
        response = self.connector.put(f'{self.endpoint_base}/{vendor_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, vendor_id, **kwargs):
        '''
        Delete a Vendor
        https://api.doorloop.com/reference/delete-vendor
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{vendor_id}', **kwargs)
        return self.validator(response).validate()
