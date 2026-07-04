#!/bin/bash
#
# Build Docker containers after code changes.

install_dir () {
  cd frontend/
}

build_dir () {
  cd ..
}

# Install Dependencies
install_dir
npm install

# Build Containers
build_dir
docker compose build