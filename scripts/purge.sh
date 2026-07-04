#!/bin/bash
#
# Clean up existing Docker images.

# Delete Existing Images
docker image rm react-template-frontend
docker image rm react-template-db
docker image rm adminer