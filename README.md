# Hash Tables

## The Problem With Arrays

What is the problem we are trying to solve?
- With a list / array it is `O(n)` to linear search and `O(log n)` for a binary search.

```python
arr = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit" ]
#        0         1        2       3      4           5              6          7    
```

- Can we do better?
YES!

lookup with `O(1)` time complexity using a magic function?
- 

## Hash Functions

What is a hash function?
- we can input a string
- it will output a number
- it has to be deterministic



## Map the hash!

The numbers that we have generated could get fairly large and we need a way to turn them in to an index of a list / array.

Think of ways to do this geven a finite size of a list to turn the number in to one clamped to a range (using the modulus %)


## Summary
Hash Table has methods / functions to put data in to it and to get data out of it

To Put:
1. Run the key string through a hashing function to get a hash value
2. Mod the hash value with the table size to get the index
3. Store the value at this index

To Get:
1. Run the key string through a hashing function to get a hash value
2. Mod the hash value with the table size to get the index
3. Return the value at this index
