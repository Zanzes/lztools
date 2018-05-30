class BSSession(object):
    _status = None
    _browser_url = None
    _project_name = None
    _name = None
    _logs = None
    _public_url = None
    _reason = None
    _build_name = None
    _os_version = None
    _browser_version = None
    _device = None
    _video_url = None
    _duration = None
    _hashed_id = None
    _har_logs_url = None
    _os = None
    _browser_console_logs_url = None
    _browser = None
    _date = None

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value

    @property
    def browser_url(self):
        return self._browser_url
    @browser_url.setter
    def browser_url(self, value):
        self._browser_url = value

    @property
    def project_name(self):
        return self._project_name
    @project_name.setter
    def project_name(self, value):
        self._project_name = value

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def logs(self):
        return self._logs
    @logs.setter
    def logs(self, value):
        self._logs = value

    @property
    def public_url(self):
        return self._public_url
    @public_url.setter
    def public_url(self, value):
        self._public_url = value

    @property
    def reason(self):
        return self._reason
    @reason.setter
    def reason(self, value):
        self._reason = value

    @property
    def build_name(self):
        return self._build_name
    @build_name.setter
    def build_name(self, value):
        self._build_name = value

    @property
    def os_version(self):
        return self._os_version
    @os_version.setter
    def os_version(self, value):
        self._os_version = value

    @property
    def browser_version(self):
        return self._browser_version
    @browser_version.setter
    def browser_version(self, value):
        self._browser_version = value

    @property
    def device(self):
        return self._device
    @device.setter
    def device(self, value):
        self._device = value

    @property
    def video_url(self):
        return self._video_url
    @video_url.setter
    def video_url(self, value):
        self._video_url = value

    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def hashed_id(self):
        return self._hashed_id
    @hashed_id.setter
    def hashed_id(self, value):
        self._hashed_id = value

    @property
    def har_logs_url(self):
        return self._har_logs_url
    @har_logs_url.setter
    def har_logs_url(self, value):
        self._har_logs_url = value

    @property
    def os(self):
        return self._os
    @os.setter
    def os(self, value):
        self._os = value

    @property
    def browser_console_logs_url(self):
        return self._browser_console_logs_url
    @browser_console_logs_url.setter
    def browser_console_logs_url(self, value):
        self._browser_console_logs_url = value

    @property
    def browser(self):
        return self._browser
    @browser.setter
    def browser(self, value):
        self._browser = value

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        self._date = value

