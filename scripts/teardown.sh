#!/bin/bash
#
# Tear down container resources.

docker compose down
sleep 5
docker container prune --force
