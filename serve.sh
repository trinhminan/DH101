#!/bin/bash
# Simple script to serve the website locally

echo "Starting local server..."
echo "Visit: http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""

python3 -m http.server 8000
