import os
import mimetypes
from requests_toolbelt.multipart.encoder import MultipartEncoder

from .base import DoorLoopBase


class DoorLoopFile(DoorLoopBase):
    endpoint_base = '/files'
    RESOURCE_TYPES = [
        'TENANT',
        'OWNER',
        'VENDOR',
        'PROPERTY',
        'UNIT',
        'LEASE',
        'LEASE_DRAFT',
        'TASK',
        'RENTAL_APPLICATION',
        'BILL',
        'BILL_PAYMENT',
        'VENDOR_CREDIT',
        'NOTE',
        'INSURANCE_POLICY',
        'COMMUNICATION'
    ]

    @staticmethod
    def prepare_multipart_payload(data, file_path):
        mime_type, _ = mimetypes.guess_type(file_path)
        fields = {
            'file': (
                os.path.basename(file_path),
                open(file_path, 'rb'),
                mime_type,
            ),
            'name': data['name'],
            'linkedResource[resourceId]': data['linkedResource']['resourceId'],
            'linkedResource[resourceType]': data['linkedResource']['resourceType'],
        }
        # Add dict values as form fields
        if data.get('notes'):
            fields.update({'notes': data['notes']})
        if data.get('tags'):
            i = 0
            for tag in data['tags']:
                fields.update({f"tag{i}": tag})
        if data.get('createdBy'):
            fields.update({'createdBy': data['createdBy']})
        return MultipartEncoder(
            fields=fields
        )

    def list(self, **kwargs):
        '''
        List all Files
        https://api.doorloop.com/reference/get-files
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def upload(self, data, file_path, **kwargs):
        '''
        Upload a File
        https://api.doorloop.com/reference/post-files
        '''
        multipart_data = self.prepare_multipart_payload(data, file_path)
        kwargs['headers'] = {
            'Accept': None,
            'Content-Type': multipart_data.content_type,
        }
        response = self.connector.post(f'{self.endpoint_base}', multipart_data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, file_id, **kwargs):
        '''
        Retrieve a File
        https://api.doorloop.com/reference/get-file
        '''
        response = self.connector.get(f'{self.endpoint_base}/{file_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, file_id, data, file_path, **kwargs):
        '''
        Update a File
        https://api.doorloop.com/reference/put-file
        '''
        multipart_data = self.prepare_multipart_payload(data, file_path)
        kwargs['headers'] = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': multipart_data.content_type,
        }
        response = self.connector.put(f'{self.endpoint_base}/{file_id}', multipart_data, **kwargs)
        return self.validator(response).validate()

    def delete(self, file_id, **kwargs):
        '''
        Delete a File
        https://api.doorloop.com/reference/delete-file
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{file_id}', **kwargs)
        return self.validator(response).validate()

    def download(self, file_id, **kwargs):
        '''
        Download a File
        https://api.doorloop.com/reference/download-file
        '''
        response = self.connector.get(f'{self.endpoint_base}/{file_id}/download', **kwargs)
        return self.validator(response).validate()
