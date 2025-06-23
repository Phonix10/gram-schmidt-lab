import numpy as np

def gram_schmidt(vectors, orthonormal=False, tol=1e-10):
    basis = []
    for v in vectors:
        v = np.array(v, dtype=float)
        for u in basis:
            proj = np.dot(v, u) / np.dot(u, u) * u
            v = v - proj
        norm = np.linalg.norm(v)
        if norm > tol:
            basis.append(v / norm if orthonormal else v)
    return np.array(basis)

def get_user_input():
    print("Gram-Schmidt Orthogonalization Tool")
    num_vectors = int(input("Enter the number of vectors: "))
    dim = int(input("Enter the dimension of each vector: "))
    
    vectors = []
    for i in range(num_vectors):
        while True:
            try:
                raw = input(f"Enter vector {i+1} as {dim} space-separated numbers: ")
                vector = list(map(float, raw.strip().split()))
                if len(vector) != dim:
                    print(f"❌ Vector must have exactly {dim} values.")
                    continue
                vectors.append(vector)
                break
            except ValueError:
                print("❌ Invalid input. Please enter only numbers.")
    
    return np.array(vectors)

if __name__ == "__main__":
    vectors = get_user_input()
    
    choice = input("Do you want orthonormal basis? (y/n): ").strip().lower()
    orthonormal = choice == 'y'

    result = gram_schmidt(vectors, orthonormal=orthonormal)

    print("\n✅ Resulting", "Orthonormal" if orthonormal else "Orthogonal", "Vectors:")
    for i, vec in enumerate(result):
        print(f"Vector {i+1}: {vec}")