from rest_framework.exceptions import APIException


# let's make custom exception handler

class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "The requested profile does not exist"


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You can't edit a profile doesn't belong to you"
