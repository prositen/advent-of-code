#!/usr/bin/env bash
source ../common.bash

function count_decreases() {
  local prev_depth=0
  local decreases=0
  local window_size=$1
  for i1 in "${!dec01_input[@]}"; do
    local depth=0
    for ((i2=0;i2 < window_size;i2++)); do
      local term=${dec01_input[((i1 + i2))]}
      ((depth += term))
    done
    if ((prev_depth > 0)); then
      if ((depth > prev_depth)); then
        ((decreases += 1))
      fi
    fi
    ((prev_depth = depth))
  done
  echo "${decreases}"
}

function dec01_test() {
  dec01_input=("199" "200" "208" "210" "200" "207" "240" "269" "260" "263")
  (( $(count_decreases 1)==7)) || return 1
  (( $(count_decreases 3)==5)) || return 1
}

function dec01_main() {
  declare -a dec01_input
  read_file_to_arr 2021 1 dec01_input
  echo "Part 1: $(count_decreases 1)"
  echo "Part 2: $(count_decreases 3)"
}

if [ "x$1" == "xtest" ]; then
    dec01_test
else
    dec01_main
fi
