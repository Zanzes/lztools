from pprint import pprint
import ScratchPad, lztools, A, B

from lztools.modules import get_module_path

# print("A:")
# pprint(A.__dict__)
# print("")
# print("B:")
# pprint(B.__dict__)

class C(object):
    a = 1

print(get_module_path(A))
print(get_module_path(B))
print(get_module_path(C))
print(get_module_path(C()))
print(get_module_path(ScratchPad))
print(get_module_path(2))
