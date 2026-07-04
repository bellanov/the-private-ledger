#!/bin/bash
#
# Redeploy the application by tearing down, purging, building, and deploying.

scripts/teardown.sh
scripts/build.sh
scripts/deploy.sh
