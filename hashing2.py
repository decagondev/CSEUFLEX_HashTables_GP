# hashtableentry class 
# key, value
# repr
# str

class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def repr(self):
        return f"HashTableEntry({self.key}, {self.value})"



hash_table = [None] * 8   # 8 slots, all initiailized to None

def my_hash(s):
    sb = s.encode()  # Get the UTF-8 bytes for the string

    total = 0

    for b in sb:
        total += b
        total &= 0xffffffff  # clamp to 32 bits

    return total

def hash_index(key):
    h = my_hash(key)
    return h % len(hash_table)

def put(key, val):
    i = hash_index(key)
    if hash_table[i] != None:
        print(f"Collision! Overwriting {repr(hash_table[i])}")
    hash_table[i] = HashTableEntry(key, val)
    
def get(key):
    i = hash_index(key)
    entry = hash_table[i]

    if entry == None:
        return None

    return entry.value

def delete(key):
    i = hash_index(key)
    hash_table[i] = None

    
put("Hello", "Hello Value")
put("World", "World Value")
put("foo", "foo value")   # "foo" hashes to same index as "Hello"
                          # AKA "foo collides with Hello"

print(hash_table)

v = get("Hello")
print(f'Hello value is: {v}') # Should be "Hello Value", but gives "foo value"

# Get "Frogs" from the table
# Doesn't exist!
v = get("Frogs")
print(v)  # "None"