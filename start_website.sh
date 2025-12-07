#!/bin/bash
# Start the HCI Study Website

echo "🚀 Starting HCI Study Website..."
echo ""
echo "The website will open at: http://localhost:8000"
echo "Press Ctrl+C to stop the server when you're done studying."
echo ""

# Start the server and open browser
python3 -m http.server 8000 &
SERVER_PID=$!

# Wait a moment for server to start
sleep 2

# Open in browser
open http://localhost:8000

# Wait for user to stop
wait $SERVER_PID
