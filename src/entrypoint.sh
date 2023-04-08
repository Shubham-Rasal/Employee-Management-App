#!/bin/bash
set -e

# Remove a potentially pre-existing server.pid for Rails.
rm -f /myapp/tmp/pids/server.pid

#print in the console after successful removal of server.pid
echo "server.pid removed"

# Then exec the container's main process (what's set as CMD in the Dockerfile).
exec "$@"