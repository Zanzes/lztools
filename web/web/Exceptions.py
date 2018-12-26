class ElementVisibilityTimeout(Exception):
    def __init__(self, message, **kwargs):
        super(ElementVisibilityTimeout, self).__init__(message, **kwargs)

class APIRequestException(Exception):
    def __init__(self, message, **kwargs):
        super(APIRequestException, self).__init__(message, **kwargs)


class SettingsFieldException(Exception):
    def __init__(self, message, field=None, **kwargs):
        if field is not None:
            message += f" (Name: {field.name}, Id: {field.id}, Group: {field.group_id})"
        super(SettingsFieldException, self).__init__(message, **kwargs)

class ImplementationException(Exception):
    def __init__(self, message, **kwargs):
        super(ImplementationException, self).__init__(message, **kwargs)

class UploadException(Exception):
    def __init__(self, message, **kwargs):
        super(UploadException, self).__init__(message, **kwargs)

class FieldValueError(Exception):
    def __init__(self, message, **kwargs):
        super(FieldValueError, self).__init__(message, **kwargs)