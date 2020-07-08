def letter_count(s):
    d = {}

    for c in s:

        if c.isspace():
            continue
        
        c = c.lower()

        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    return d

def print_sorted_count(s):
    count = letter_count(s)

    items = list(count.items())

    items.sort(key=lambda e: e[1], reverse=True)

    for i in items:
        print(f"{i[0]}: {i[1]}")


my_string = "aabcDcc dd      ddd D"

print(letter_count(my_string))
print_sorted_count(my_string)

