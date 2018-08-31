import scratch
from lztools.extensions import get_variable_type_hint
from lztools.text import as_literal
m9:int = "123"
m8:123 = "123"
m7 = "123"
m6:int = None
print(f"m1: {get_variable_type_hint(scratch.m1)}")
print(f"m2: {get_variable_type_hint(scratch.m2)}")
print(f"m3: {get_variable_type_hint(scratch.m3)}")
print(f"m4: {get_variable_type_hint(scratch.Holder.m4)}")
print(f"m6: {get_variable_type_hint(m6)}")
print(f"m7: {get_variable_type_hint(m7)}")
print(f"m8: {get_variable_type_hint(m8)}")
print(f"m9: {get_variable_type_hint(m9)}")
print(f"m1: {as_literal(scratch.m1)}")
print(f"m2: {as_literal(scratch.m2)}")
print(f"m3: {as_literal(scratch.m3)}")