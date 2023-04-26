import os

from .base import DoorLoopTestCase


class TestFiles(DoorLoopTestCase):

    def setUp(self):
        resp = self.dl.properties.list(query_params={'page_size': 100})
        self.resource_id = resp['data'][0]['id']

    def test_upload_file(self):
        resp = self.dl.files.upload(
            data={
                'name': 'test-file.pdf',
                'linkedResource': {
                    'resourceId': self.resource_id,
                    'resourceType': "PROPERTY",
                },
            },
            file_path='tests/test-file.pdf'
        )
        assert isinstance(resp, dict)
        assert resp['downloadUrl']
