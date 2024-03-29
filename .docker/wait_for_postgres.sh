#!/usr/bin/env bash
# wait-for-postgres.sh

set -e

cmd="$@"


until PGPASSWORD=postgres psql -h db --username=postgres develops_today -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd