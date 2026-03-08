#!/bin/sh

echo "Waiting for database..."

sleep 3

echo "Running migrations..."

flask db upgrade

echo "Seeding database..."

python seed.py

echo "Starting Flask..."

flask run --host=0.0.0.0 --port=5000