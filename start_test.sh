#!/bin/bash

# Start the Django development server
python3.10 cls_server/manage.py runserver &

# Wait for the server to start (adjust the sleep time as needed)
sleep 5

# Run the Django tests
python3.10 cls_server/manage.py test tests

# Get the process ID (PID) of the main Django process
server_pid=$(ps aux | grep manage.py | grep runserver | awk '{print $2}')

# Check if the server process is still running
if [[ -n "$server_pid" ]]; then
    # Terminate the server process using its PID
    kill $server_pid
    echo "Terminating Django development server (PID: $server_pid)"

    # Wait for the server to gracefully shut down (adjust the sleep time as needed)
    sleep 5

    # Check if the server process is still running (after waiting for graceful shutdown)
    if [[ $(ps -p $server_pid | wc -l) -gt 1 ]]; then
        echo "Graceful shutdown failed. Forcing termination..."
        kill -9 $server_pid
    fi
fi