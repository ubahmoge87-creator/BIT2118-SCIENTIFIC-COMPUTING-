
import numpy as np

print("TASK 9: EIGENVALUES AND EIGENVECTORS")

A = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
], dtype=float)

# Original example: network connections
values, vectors = np.linalg.eig(A)
idx = np.argmax(values.real)
largest_value = values[idx].real
centrality = np.abs(vectors[:, idx].real)
centrality = centrality / centrality.sum()

print("\nOriginal eigenvalues:", np.round(values.real, 4))
print("Largest eigenvalue:", round(largest_value, 4))
print("Node centrality scores:", np.round(centrality, 4))

# Modification: add a connection between nodes A and D
modified_A = A.copy()
modified_A[0, 3] = 1
modified_A[3, 0] = 1

mod_values, mod_vectors = np.linalg.eig(modified_A)
mod_idx = np.argmax(mod_values.real)
mod_centrality = np.abs(mod_vectors[:, mod_idx].real)
mod_centrality /= mod_centrality.sum()

print("\nModified adjacency matrix:\n", modified_A)
print("Modified largest eigenvalue:", round(mod_values[mod_idx].real, 4))
print("Modified centrality scores:", np.round(mod_centrality, 4))

# Related application: rank four connected service stations
station_names = ["A", "B", "C", "D"]
ranking = sorted(zip(station_names, centrality),
                 key=lambda item: item[1], reverse=True)

print("\nService station importance ranking:")
for name, score in ranking:
    print(name, round(score, 4))
