"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""

# YOUR CODE HERE

for first in ["c", "t", "b" ]:
    for second in ["a", "o"]:
        for third in ["p", "t", "n"]:
            print(first+second+third)
            








