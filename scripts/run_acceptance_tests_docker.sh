#!/usr/bin/env bash

set -e

cleanup()
{
    docker-compose -f docker-compose-test.yml down
}

trap 'cleanup' ERR EXIT INT

this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
root_dir="${this_dir}/.."

cd $root_dir

./scripts/build_docker.sh

docker-compose -f docker-compose-test.yml up -d

docker exec -i -w /build vending-machine-tests ./scripts/run_acceptance_tests.sh
