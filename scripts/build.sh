#!/bin/bash
#
# Build Docker containers after code changes.

cd_install_dir () {
  cd frontend/web
}

cd_build_dir () {
  cd ..
}

# Install Dependencies
cd_install_dir
npm install

# Build Containers
cd_build_dir
docker compose build