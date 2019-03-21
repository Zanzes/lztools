def get_public_attributes(obj):
    for item in obj.__dict__:
        if not item.startswith("_"):
            yield item

def try_call(item, method, *args, **kwargs):
    if hasattr(item, method):
        call = getattr(item, method)
        if callable(call):
            return call(*args, **kwargs)