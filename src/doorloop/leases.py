from .base import DoorLoopBase


class DoorLoopLease(DoorLoopBase):
    endpoint_base = '/leases'

    def list(self, **kwargs):
        '''
        List all Leases
        https://api.doorloop.com/reference/get-leases
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def retrieve(self, lease_id, **kwargs):
        '''
        Retrieve a Lease
        https://api.doorloop.com/reference/get-lease
        '''
        response = self.connector.get(f'{self.endpoint_base}/{lease_id}', **kwargs)
        return self.validator(response).validate()

    def move_in_tenant(self, data, **kwargs):
        '''
        Move in Tenant
        https://api.doorloop.com/reference/post-leases-move-in
        '''
        response = self.connector.post(f'{self.endpoint_base}/move-in', data, **kwargs)
        return self.validator(response).validate()

    def move_out_tenant(self, data, **kwargs):
        '''
        Move out Tenant
        https://api.doorloop.com/reference/post-leases-move-out
        '''
        response = self.connector.post(f'{self.endpoint_base}/move-out', data, **kwargs)
        return self.validator(response).validate()

    def list_lease_tenants(self, lease_id, **kwargs):
        '''
        List all Lease Tenants
        https://api.doorloop.com/reference/get-lease-tenants
        '''
        response = self.connector.get(f'{self.endpoint_base}/{lease_id}/lease-tenants', **kwargs)
        return self.validator(response).validate()
