#!/bin/bash
# Simple script to serve the website locally

echo "Starting local server..."
echo "Press Ctrl+C to stop the server"
echo ""

if command -v bundle >/dev/null 2>&1 && [ -f "Gemfile" ]; then
	echo "Using Jekyll (recommended): http://localhost:4000"
	bundle exec jekyll serve --livereload
elif command -v jekyll >/dev/null 2>&1; then
	echo "Using Jekyll (recommended): http://localhost:4000"
	jekyll serve --livereload
else
	echo "Jekyll not found. Falling back to static server: http://localhost:8000"
	echo "Note: Markdown/Liquid pages may not render correctly in static mode."
	python3 -m http.server 8000
fi
