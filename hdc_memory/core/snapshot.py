import os
import pickle
from datetime import datetime

def save_snapshot(hdc, name="latest"):
    """Speichert den aktuellen Speicherzustand als Pickle-Datei"""
    if not os.path.exists("snapshots"):
        os.makedirs("snapshots")
    
    filename = f"snapshot_{name}.pkl"
    filepath = os.path.join("snapshots", filename)

    with open(filepath, "wb") as f:
        pickle.dump(hdc, f)

    print(f"💾 Snapshot gespeichert unter: {filename}")

def load_snapshot(hdc, name="latest"):
    """Lädt einen zuvor gespeicherten Snapshot"""
    filepath = os.path.join("snapshots", f"snapshot_{name}.pkl")

    if not os.path.exists(filepath):
        print(f"❌ Snapshot {name} nicht gefunden.")
        return

    with open(filepath, "rb") as f:
        data = pickle.load(f)

    hdc.__dict__.update(data.__dict__)
    print(f"📦 Snapshot {name} erfolgreich geladen.")
