#!/usr/bin/env bash
source ../common.bash

function two_entries() {
  local product=0
  local sorted
  sort_arr sorted "${dec01_input[*]}"
  for i1 in "${!sorted[@]}"; do
    for i2 in "${!sorted[@]}"; do
      local a=${sorted[$i1]}
      local b=${sorted[$i2]}
      if (( (a+b) == 2020 )); then
        ((product = a*b))
        echo ${product}
        return
      fi
    done
  done
  echo 0
}

function three_entries() {
  local product=0
  local sorted
  sort_arr sorted "${dec01_input[*]}"
  for i1 in "${!sorted[@]}"; do
    for i2 in "${!sorted[@]}"; do
      for i3 in "${!sorted[@]}"; do
        local a=${sorted[$i1]}
        local b=${sorted[$i2]}
        local c=${sorted[$i3]}
        if (( (a+b+c) == 2020 )); then
          ((product = a*b*c))
          echo ${product}
          return
        fi
      done
    done
  done
  echo 0
}

function dec01_test() {
  dec01_input=("1721" "979" "366" "299" "675" "1456")
  (( $(two_entries) == 514579 )) | return 1

  (( $(three_entries) == 241861950 )) | return 1
  return 0
}

function dec01_main() {
  declare -a dec01_input
  read_file_to_arr 2020 1 dec01_input
  echo "Part 1: $(two_entries)"
  echo "Part 2: $(three_entries)"
}

if [ "x$1" == "xtest" ]; then
    dec01_test
else
    dec01_main
fi
