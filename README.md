# hdclarity

# 🧠 HDClarity – Semantischer Vektorspeicher & API

HDClarity ist ein speicheroptimierter Hyperdimensional Memory, der numerische und kategoriale Daten zu Vektoren verarbeitet und clusteringfähig macht. Der integrierte FastAPI-Webserver erlaubt Analyse & Visualisierung über ein REST-Interface.

## Features

- 🌐 FastAPI Webservice mit Cluster-Analyse
- 🧠 Vektorisierung numerischer & kategorischer Daten
- 🔍 KMeans-Clustering & Silhouette-Bewertung
- 📦 Snapshot-basiertes Memory-Management (.pkl)
- 📊 Visualisierungen geplant (webUI)

## Setup

```bash
git clone https://github.com/schwarer2006/hdclarity.git
cd hdclarity
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
