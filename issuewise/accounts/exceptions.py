from rest_framework.exceptions import APIException
from rest_framework import status

class UserNotActive(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    def __init__(self, explanation):
        if explanation == 'NV':
            self.detail = 'Email of user is not verified'
        
        elif explanation == 'AB':
            self.detail == 'Account is blocked'
        
        elif explanation == 'AD':
            self.detail == 'Account is deactivated' 