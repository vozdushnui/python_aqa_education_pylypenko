# intersection
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print("The intersection of a and b:")
print("using .intersection")
print(a.intersection(b))
print(b.intersection(a))
print("using &")
print(a&b)

# symmetric_difference

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print("The symmetric_difference of a and b:")
print("using .symmeetric_difference")
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print("using ^")
print(a^b)

# difference
print("The difference of a and b:")
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])


print("The difference of a and b:")
print("using .differecne")
print(a.difference(b))
print(b.difference(a))
print("    using -")
print(a-b)
print(b-a)

# union
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print("The union of a and b")
print("using .union")
print(a.union(b))
print("using |")
print(a|b)
