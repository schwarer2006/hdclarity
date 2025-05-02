#!/bin/bash

REPO_URL="https://github.com/schwarer2006/hdclarity.git"

function show_menu() {
  echo "📦 GIT-MENÜ:"
  echo "1. Status anzeigen"
  echo "2. Dateien hinzufügen (git add .)"
  echo "3. Commit ausführen"
  echo "4. Push nach GitHub"
  echo "5. Pull von GitHub"
  echo "6. Git-Konfiguration anzeigen"
  echo "7. Remote setzen oder ändern"
  echo "8. Beenden"
}

function git_status() {
  git status
}

function git_add() {
  git add .
  echo "✅ Dateien hinzugefügt."
}

function git_commit() {
  read -p "💬 Commit-Nachricht: " msg
  git commit -m "$msg"
}

function git_push() {
  git push -u origin main
}

function git_pull() {
  git pull origin main
}

function git_config() {
  git config --list
}

function git_remote_set() {
  read -p "🔐 GitHub Token (ohne https://...): " token
  git remote remove origin 2>/dev/null
  git remote add origin "https://$token@github.com/schwarer2006/hdclarity.git"
  echo "✅ Remote gesetzt mit Token."
}

while true; do
  show_menu
  read -p "Bitte wählen [1-8]: " choice
  case $choice in
    1) git_status ;;
    2) git_add ;;
    3) git_commit ;;
    4) git_push ;;
    5) git_pull ;;
    6) git_config ;;
    7) git_remote_set ;;
    8) echo "🚪 Verlasse das Menü."; break ;;
    *) echo "❌ Ungültige Auswahl." ;;
  esac
  echo ""
done
