# main.py im Projektverzeichnis

from core.hdc_memory import HDCMemory
from core.clustering import perform_clustering
from core.io import load_data
from core.snapshot import save_snapshot

def main():
    hdc = HDCMemory(dimension=6000)

    # Beispiel: Daten aus CSV laden
    load_data(hdc, filepath="data/sales.csv", max_rows=10000)

    # Clustering
    perform_clustering(hdc, n_clusters=10)

    # Snapshot speichern
    save_snapshot(hdc, name="init")

if __name__ == "__main__":
    main()
