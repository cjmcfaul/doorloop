from .base import DoorLoopBase


class DoorLoopVendorBill(DoorLoopBase):
    endpoint_base = '/vendor-bills'
    
    def list(self, **kwargs):
        '''
        List all Vendor Bills
        https://api.doorloop.com/reference/get-vendor-bills
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Vendor Bill
        https://api.doorloop.com/reference/post-vendor-bill
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, vendor_bill_id, **kwargs):
        '''
        Retrieve a Vendor Bill
        https://api.doorloop.com/reference/get-vendor-bill
        '''
        response = self.connector.get(f'{self.endpoint_base}/{vendor_bill_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, vendor_bill_id, data, **kwargs):
        '''
        Update a Vendor Bill
        https://api.doorloop.com/reference/put-vendor-bill
        '''
        response = self.connector.put(f'{self.endpoint_base}/{vendor_bill_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, vendor_bill_id, **kwargs):
        '''
        Delete a Vendor Bill
        https://api.doorloop.com/reference/delete-vendor-bill
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{vendor_bill_id}', **kwargs)
        return self.validator(response).validate()
