records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]


def build_index(rec):
    # build the index from the list
    pass


idx = build_index(records)

# print all the departments
for i in idx:
    print(i)

# print everyone in Engineering:
print(idx["Engineering"])