#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE evdata_e2e_test;
	GRANT ALL PRIVILEGES ON DATABASE evdata_e2e_test TO evdata;
EOSQL
