# Write a program to demonstrate all set operations (union, intersection, etc.). 
# Define two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# Union
print("\nUnion (A | B):", A | B)
print("Union using method:", A.union(B))

# Intersection
print("\nIntersection (A & B):", A & B)
print("Intersection using method:", A.intersection(B))

# Difference
print("\nDifference (A - B):", A - B)
print("Difference using method:", A.difference(B))

print("\nDifference (B - A):", B - A)

# Symmetric Difference
print("\nSymmetric Difference (A ^ B):", A ^ B)
print("Symmetric Difference using method:", A.symmetric_difference(B))

# Subset
print("\nIs A subset of B?", A.issubset(B))
print("Is {4,5} subset of A?", {4, 5}.issubset(A))

# Superset
print("Is A superset of B?", A.issuperset(B))

# Disjoint
print("\nAre A and B disjoint?", A.isdisjoint(B))
print("Are {10, 11} and A disjoint?", {10, 11}.isdisjoint(A))
