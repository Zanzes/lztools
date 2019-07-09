class ElementVisibilityTimeout(Exception):
    def __init__(self, message, **kwargs):
        super(ElementVisibilityTimeout, self).__init__(message, **kwargs)