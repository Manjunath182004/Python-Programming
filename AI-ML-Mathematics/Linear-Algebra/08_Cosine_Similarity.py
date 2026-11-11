"""
Cosine similarity:

it used in NLP, Search Engines, Recommendations system, Generative AI

Cosine similarity measures the angle-based similarity between two vectors.
"""

import math

def cosine_similarity(u, v):
    if len(u) != len(v):
        raise ValueError("Vectors must have equal dimensions")

    dot = sum(u[i] * v[i] for i in range(len(u)))

    magnitude_u = math.sqrt(sum(x**2 for x in u))
    magnitude_v = math.sqrt(sum(x**2 for x in v))

    if magnitude_u == 0 or magnitude_v == 0:
         raise ValueError("Cosine similarity is undefined for zero vectors")

    return dot / (magnitude_u * magnitude_v)

u = [1, 2]
v = [2, 4]

print("Cosine similarity:", cosine_similarity(u, v))

# using Numpy

import numpy as np

def cosine_similarity(u, v):
    u = np.array(u)
    v = np.array(v)

    denominator = np.linalg.norm(u) * np.linalg.norm(v)

    if denominator == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors")

    return np.dot(u, v) / denominator


u = np.array([1, 2])
v = np.array([2, 4])

print("Cosine similarity:", cosine_similarity(u, v))


# Examples:

vectors = [
    ([1, 0], [1, 0]),       # Same direction
    ([1, 0], [0, 1]),       # Orthogonal
    ([1, 0], [-1, 0]),      # Opposite direction
    ([1, 2], [2, 4]),       # Same direction
    ([1, 2], [2, 1])        # Different directions
]

for u, v in vectors:
    u = np.array(u)
    v = np.array(v)

    similarity = np.dot(u, v) / (
        np.linalg.norm(u) * np.linalg.norm(v)
    )

    print(u, v, "=>", round(similarity, 4))


# another ex: 

king = np.array([0.29, 0.68])
queen = np.array([0.51, 0.71])
apple = np.array([0.10, 0.20])
banana = np.array([0.12, 0.22])

def similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("King vs Queen:", similarity(king, queen))
print("Apple vs Banana:", similarity(apple, banana))
print("King vs Apple:", similarity(king, apple))