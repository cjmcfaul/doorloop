from .base import DoorLoopBase


class DoorLoopTask(DoorLoopBase):
    endpoint_base = '/tasks'

    def list(self, **kwargs):
        '''
        Retrieve all Tasks
        https://api.doorloop.com/reference/get-tasks
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Task
        https://api.doorloop.com/reference/post-task
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def post_update(self, data, **kwargs):
        '''
        Post an Update on a Task
        https://api.doorloop.com/reference/post-task-update
        '''
        response = self.connector.post(f'{self.endpoint_base}/update', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, task_id, **kwargs):
        '''
        Retrieve a Task
        https://api.doorloop.com/reference/get-task
        '''
        response = self.connector.get(f'{self.endpoint_base}/{task_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, task_id, data, **kwargs):
        '''
        Update a Task
        https://api.doorloop.com/reference/put-task
        '''
        response = self.connector.put(f'{self.endpoint_base}/{task_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, task_id, **kwargs):
        '''
        Deletes a Task
        https://api.doorloop.com/reference/delete-task
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{task_id}', **kwargs)
        return self.validator(response).validate()