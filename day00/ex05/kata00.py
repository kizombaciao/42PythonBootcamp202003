# string formatting

t = (19, 42, 21)
print(f"The {len(t)} numbers are: {' '.join([str(elem) for elem in t])}")

# str() converts number into a string