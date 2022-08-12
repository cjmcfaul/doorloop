from .base import DoorLoopBase


class DoorLoopTenant(DoorLoopBase):
    endpoint_base = '/tenants'
    STATUSES = (
        ('Past', 'PAST'),
        ('Current', 'CURRENT'),
        ('Future', 'FUTURE'),
    )

    def retrieve(self, tenant_id, **kwargs):
        '''
        Retrieve a Tenant
        https://api.doorloop.com/reference/get-tenant
        '''
        response = self.connector.get(f'{self.endpoint_base}/{tenant_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, tenant_id, data, **kwargs):
        '''
        Update a Tenant
        https://api.doorloop.com/reference/put-tenant
        '''
        response = self.connector.put(f'{self.endpoint_base}/{tenant_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, tenant_id, **kwargs):
        '''
        Delete a Tenant
        https://api.doorloop.com/reference/delete-tenant
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{tenant_id}', **kwargs)
        return self.validator(response).validate()

    def list(self, **kwargs):
        '''
        Retrieve all Tenants
        https://api.doorloop.com/reference/get-tenants
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create_prospect(self, data, **kwargs):
        '''
        Create a Prospect
        https://api.doorloop.com/reference/post-tenant
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()
