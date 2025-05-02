import numpy as np
import hashlib
from sklearn.cluster import KMeans

class HDCMemoryStorage:
    def __init__(self, dimension=6000):
        self.dimension = dimension
        self.vectors = []
        self.id_to_meta = {}
        self.index_to_id = {}
        self.id_to_index = {}
        self.id_to_hash = {}
        self.feature_map = {}
        self.field_types = {}

    def set_field_types(self, field_types: dict):
        """Definiert, welche Felder numerisch oder kategorisch sind"""
        self.field_types = field_types

    def _get_position(self, feature_name):
        if feature_name not in self.feature_map:
            self.feature_map[feature_name] = np.random.randint(0, self.dimension)
        return self.feature_map[feature_name]

    def _vectorize(self, data: dict) -> np.ndarray:
        vec = np.zeros(self.dimension)

        for key, value in data.items():
            ftype = self.field_types.get(key)
            if ftype == "numeric" and isinstance(value, (int, float)):
                idx = self._get_position(key)
                vec[idx] = value
            elif ftype == "categorical" and isinstance(value, str):
                idx = self._get_position(f"{key}_{value}")
                vec[idx] = 1.0

        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec

    def _hash_data(self, data: dict) -> str:
        data_str = str(sorted(data.items()))
        return hashlib.sha256(data_str.encode()).hexdigest()

    def add(self, uid: str, data: dict):
        if uid in self.id_to_index:
            print(f"⚠️ ID {uid} existiert bereits – übersprungen.")
            return
        vec = self._vectorize(data)
        idx = len(self.vectors)
        self.vectors.append(vec)
        self.index_to_id[idx] = uid
        self.id_to_index[uid] = idx
        self.id_to_meta[uid] = data
        self.id_to_hash[uid] = self._hash_data(data)

    def cluster(self, n_clusters=5):
        """Bildet Cluster mit KMeans"""
        matrix = np.array(self.vectors)
        if len(matrix) == 0:
            print("⚠️ Keine Vektoren vorhanden.")
            return
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
        self.cluster_labels = self.kmeans.fit_predict(matrix)
        print(f"✅ Clusterbildung abgeschlossen: {n_clusters} Gruppen.")

    def create_supervectors(self):
        """Berechnet Supervektoren (Zentren der Cluster)"""
        if not hasattr(self, "cluster_labels"):
            print("⚠️ Keine Cluster vorhanden. Bitte zuerst clustern.")
            return

        clusters = {}
        for idx, label in enumerate(self.cluster_labels):
            clusters.setdefault(label, []).append(self.vectors[idx])

        self.supervectors = {}
        for label, vecs in clusters.items():
            summed_vector = np.sum(vecs, axis=0)
            norm = np.linalg.norm(summed_vector)
            self.supervectors[label] = summed_vector / norm if norm > 0 else summed_vector

        print(f"✅ Supervektoren für {len(self.supervectors)} Cluster erstellt.")

print("🧠 HDClarity Memory Core geladen.")
