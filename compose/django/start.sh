#!/bin/bash
function manage_app () {
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --no-input
}

function start_development() {
    # use django runserver as development server here.
    manage_app
    python manage.py runserver 0.0.0.0:8000
}

# use development server
start_development
