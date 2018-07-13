import inspect
import gc

def get_variable_name():
    f = inspect.currentframe().f_back.f_back
    filename = inspect.getfile(f)
    code_line = open(filename).readlines()[f.f_lineno - 1]
    assigned_variable = code_line.split("=")[0].strip()
    return assigned_variable

def find_names(self):
    frame = inspect.currentframe()
    for frame in iter(lambda: frame.f_back, None):
        frame.f_locals
    obj_names = []
    for referrer in gc.get_referrers(self):
        if isinstance(referrer, dict):
            for k, v in referrer.items():
                if v is self:
                    obj_names.append(k)
    print(obj_names)