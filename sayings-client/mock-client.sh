#!/bin/sh

# Do some shell chicanery to make this mock client interruptible by signals.
# Also catch SIGHUP and explicitly `exit` because Busybox's `ash` shell
# behaves differently as PID 1, which is the case inside the container.
trap '[ $pid ] && kill $pid; echo "[$(date)] Stopping mock client."; exit' \
     INT HUP TERM

echo "[$(date)] Hello! Starting mock client..."
echo "This is our IP interface(s) configuration:"
ip address show
sleep 2

echo "Commencing while-loop querying of sayings API server..."
while :; do
    curl -s "${API_ADDRESS:-127.0.0.1:8080}/" | jq '.'

    # Continue chicanery: we background the `sleep` and `wait` on it to
    # complete. Signals don't interrupt sleep, but they do wait.
    sleep "${SLEEP_DURATION:-10}" & pid=$!
    wait $pid
    pid=''
done
