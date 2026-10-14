#!/bin/bash
# SA campaign: each job runs $SECS seconds
SECS=${SECS:-240}
cd /workspace/unsolved/graffiti195
mkdir -p out/sa
run(){ python3 sa.py "$@" > out/sa/$(echo "$@" | tr ' ' '_').json 2>&1; }
export -f run
for n in 12 14 16 18 20 24 28 32; do
  for v in 195c 195w; do echo "$v $n $SECS $n d3"; done
  echo "219 $n $SECS $n tf"
done | xargs -P ${P:-4} -I{} bash -c 'run {}'
