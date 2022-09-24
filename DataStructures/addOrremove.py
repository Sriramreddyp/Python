letters = ["a", "b", "c"]

# add
letters.append("d")
print(letters)

letters.insert(0, "a")

print(letters)

# remove
letters.pop()
print(letters)
letters.pop(0)
print(letters)
letters.remove("b")  # first occurence
print(letters)
del letters[0:1]
print(letters)
letters.clear()
