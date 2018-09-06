from lztools.text import print_dict, print_dir_values, print_collection

class A(object):
    x = { "joe": "smohe", "jack": 123}
    pass

    def joe(self):
        return 0

print_dict(A)
print("")
print("")
print_dict(A())
print(A().__dict__)

