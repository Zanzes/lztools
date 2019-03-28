class HTMLElementList(list):
    # def __init__(self, elements=None, *args, **kwargs):
    #     if elements is not None:
    #         for i in elements:
    #             if not isinstance(i, HTMLElement):
    #                 i = HTMLElement(i)
    #             self.append(i)
    #     else:
    #         super(HTMLElementList, self).__init__(*args, **kwargs)

    def by_attribute(self, name, value, case_sensitive=False):
        for x in self:
            if case_sensitive:
                if x.get_attribute(name) == value:
                    return x
            else:
                y = x.get_attribute(name)
                if y:
                    if y.lower() == value.lower():
                        return x

    def n_by_attribute(self, name, value, case_sensitive=False):
        for x in self:
            if case_sensitive:
                if x.get_attribute(name) == value:
                    yield x
            else:
                if x.get_attribute(name).lower() == value.lower():
                    yield x

    def by_data_template(self, value, case_sensitive=False):
        for x in self:
            if case_sensitive:
                if x.get_attribute("data-template") == value:
                    return x
            else:
                if x.get_attribute("data-template").lower() == value.lower():
                    return x

    def n_by_data_template(self, value, case_sensitive=False):
        for x in self:
            if case_sensitive:
                if x.get_attribute("data-template") == value:
                    yield x
            else:
                if x.get_attribute("data-template").lower() == value.lower():
                    yield x

