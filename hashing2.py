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
    hash_table[i] = val
    
def get(key):
    i = hash_index(key)
    return hash_table[i]

def delete(key):
    pass
    
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