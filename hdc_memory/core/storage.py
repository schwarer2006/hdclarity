# core/storage.py
import numpy as np
import hashlib
import pickle

class HDCMemoryStorage:
    def __init__(self, dimension=6000):
        self.dimension = dimension
        self.vectors = []
        self.index_to_id = {}
        self.id_to_index = {}
        self.id_to_hash = {}
        self.id_to_meta = {}
        self.feature_map = {}
        self.field_types = {}
        self.cluster_labels = None
        self.supervectors = {}

    def _get_position(self, feature_name):
        if feature_name not in self.feature_map:
            self.feature_map[feature_name] = np.random.randint(0, self.dimension)
        return self.feature_map[feature_name]

    def _vectorize(self, data):
        vec = np.zeros(self.dimension)
        for key, value in data.items():
            field_type = self.field_types.get(key)
            if field_type == "numeric" and isinstance(value, (int, float)):
                vec[self._get_position(key)] = value
            elif field_type == "categorical" and isinstance(value, str):
                vec[self._get_position(f"{key}_{value}")] = 1.0
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec

    def add(self, uid, data):
        if uid in self.id_to_index:
            return
        vec = self._vectorize(data)
        idx = len(self.vectors)
        self.vectors.append(vec)
        self.index_to_id[idx] = uid
        self.id_to_index[uid] = idx
        self.id_to_hash[uid] = self._hash_data(data)
        self.id_to_meta[uid] = data

    def _hash_data(self, data):
        s = str(sorted(data.items()))
        return hashlib.sha256(s.encode()).hexdigest()

    def set_field_types(self, field_types):
        self.field_types = field_types

    def get_vector(self, uid):
        idx = self.id_to_index.get(uid)
        return self.vectors[idx] if idx is not None else None

