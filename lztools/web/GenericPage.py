class GenericPage():
    url = None

    def __init__(self, url):
        super().__init__(url)
        self.url = url
        self.timeout = 10
        self.navigate()

    def navigate(self):
        if self.url != self.get_current_url():
            self.get(self.url)