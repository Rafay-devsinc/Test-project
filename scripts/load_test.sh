#!/usr/bin/env bash
set -e

DURATION=10s
RESULTS="load_test_results.txt"

echo "Running load test on foo.localhost and bar.localhost..."

# hey -z $DURATION -q 10 -c 5 http://foo.localhost/ > foo_results.txt
# hey -z $DURATION -q 10 -c 5 http://bar.localhost/ > bar_results.txt


hey -z 10s -q 10 -c 5 http://localhost:8081/ > load_test_results.txt
hey -z 10s -q 10 -c 5 http://localhost:8082/ >> load_test_results.txt

echo "==== FOO ====" > $RESULTS
cat foo_results.txt >> $RESULTS
echo -e "\n==== BAR ====" >> $RESULTS
cat bar_results.txt >> $RESULTS

cat $RESULTS
