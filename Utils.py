def init_data_object(object_type, values):
    if object_type is type:
        o = object_type()
    else:
        o = object_type

    for key in values:
        if hasattr(o, key):
            setattr(o, key, values[key])
    return o

def create_data_class(name, template_object):
    with open("{}.py".format(name), "w+") as f:
        f.write("class {}(object):\n".format(name))
        for x in template_object:
            f.write("    _{} = None\n".format(x))
        f.write("\n")
        for x in template_object:
            f.write("    @property\n")
            f.write("    def {}(self):\n".format(x))
            f.write("        return self._{}\n".format(x))
            f.write("    @{}.setter\n".format(x))
            f.write("    def {}(self, value):\n".format(x))
            f.write("        self._{} = value\n\n".format(x))






