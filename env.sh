#!/bin/bash
# The way to tidy environmet.

PROJECT_ROOT="$(pwd)"

IP="127.0.0.1"
PORT=8000

# 開発時に有用なコード達

function open-browser () {
    # Wsl2 only
    explorer.exe http://"$IP":"$PORT"/
    # ubuntu 22.04 LTS
    xdg-open http://"$IP":"$PORT"/

}


function run () {
    open-browser
    python3 "$PROJECT_ROOT"/manage.py runserver
}

function admin () {
    open-browser
    python3 "$PROJECT_ROOT"/manage.py runserver
}


function test () {
    python3 "$PROJECT_ROOT"/manage.py test
}

function migrate () {
    python3 "$PROJECT_ROOT"/manage.py makemigrations
    python3 "$PROJECT_ROOT"/manage.py migrate
}

alias py="python3"
alias mig="migrate"
