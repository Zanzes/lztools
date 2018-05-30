class BSBuild(object):
    _name = None
    _duration = None
    _status = None
    _hashed_id = None

    def __init__(self, name=None, status=None, duration=None, hashed_id=None):
        self._status = status
        self._name = name
        self._duration = duration
        self._hashed_id = hashed_id

    @property
    def hashed_id(self):
        return self._hashed_id
    @hashed_id.setter
    def hashed_id(self, value):
        self._hashed_id = value

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        self._duration = value
