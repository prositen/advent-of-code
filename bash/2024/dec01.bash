#!/usr/bin/env bash
source ../common.bash


function reconcile_lists() {
  local -a left_list
  local -a right_list
  for i1 in "${!dec01_input[@]}"; do
    local line
    read -r -a line <<< "${dec01_input[i1]}"
    left_list+=("${line[0]}")
    right_list+=("${line[1]}")
  done
  local sorted_left
  sort_arr sorted_left "${left_list[*]}"
  local sorted_right
  sort_arr sorted_right "${right_list[*]}"
  for i1 in "${!sorted_left[@]}"; do
    local left=${sorted_left[$i1]}
    local right=${sorted_right[$i1]}
    ((diff=(right-left)))
    ((sum+=$(abs ${diff})))
  done
  echo "${sum}"
}


function similarity_score() {
  local -a left_list
  local -A count
  for i1 in "${!dec01_input[@]}"; do
    local line
    read -r -a line <<< "${dec01_input[i1]}"
    left_list+=("${line[0]}")
    ((count["${line[1]}"]+=1))
  done
  local sum=0
  for n in "${left_list[@]}"; do
    ((sum+=n*count[$n]))
  done
  echo "${sum}"
}

function dec01_test() {
    # Part 1
    dec01_input=("3   4" "4   3" "2   5" "1   3" "3   9" "3   3")
    (( $(reconcile_lists) == 11)) || return 1

    # Part 2
    (( $(similarity_score) == 31)) || return 1
    return 0
}

function dec01_main() {
    declare -a dec01_input
    read_file_to_arr 2024 1 dec01_input

    echo "Part 1: $(reconcile_lists)"
    echo "Part 2: $(similarity_score)"
}

if [ "$1" == "test" ]; then
    dec01_test
else
    dec01_main
fi