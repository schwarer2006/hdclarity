# core/clustering.py
import numpy as np
from sklearn.cluster import KMeans

def perform_clustering(hdc, n_clusters=10):
    matrix = np.array(hdc.vectors)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    hdc.cluster_labels = kmeans.fit_predict(matrix)

def build_supervectors(hdc):
    from collections import defaultdict
    cluster_map = defaultdict(list)
    for idx, label in enumerate(hdc.cluster_labels):
        cluster_map[label].append(hdc.vectors[idx])
    hdc.supervectors = {
        label: np.mean(vecs, axis=0) / np.linalg.norm(np.mean(vecs, axis=0))
        for label, vecs in cluster_map.items()
    }
