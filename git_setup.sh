#!/bin/bash

# === Konfiguration ===
REPO_URL="https://github.com/schwarer2006/hdclarity.git"
BRANCH="main"
USER_NAME="schwarer2006"
USER_EMAIL="schwarer@googlemail.com"

echo "🧹 Alte Git-Konfiguration wird bereinigt..."
rm -rf .git

echo "🔁 Neues Git-Repo initialisieren..."
git init

echo "👤 Benutzerinformationen setzen..."
git config user.name "$USER_NAME"
git config user.email "$USER_EMAIL"

echo "➕ Dateien zum Commit hinzufügen..."
git add .

echo "💬 Commit erstellen..."
git commit -m "Initial project push"

echo "🌿 Branch setzen: $BRANCH"
git branch -M $BRANCH

echo "🔗 Remote-Repository verbinden..."
git remote add origin "$REPO_URL"

echo "🚀 Push auf GitHub ($REPO_URL)..."
git push -u origin $BRANCH

echo "✅ Fertig. Repository erfolgreich veröffentlicht."
