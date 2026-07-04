#!/bin/bash
#
# Install Dependencies and build Docker containers.

cd_install_dir () {
  cd frontend/web
}

cd_build_dir () {
  cd ..
}

cd_install_dir
npm install

cd_build_dir
docker compose build
