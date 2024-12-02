#!/usr/bin/env bash
source ../common.bash

function is_safe() {
  local -a report
  read -r -a report <<< "${1}"
  local prev="${report[0]}"
  local sgn_prev=
  local safe=1
  for item in "${report[@]:1}"; do
    ((diff=prev-item))
    abs_diff=$(abs ${diff})
    sgn_diff=$(sgn ${diff})
    if [[ -n ${sgn_prev} && ${sgn_diff} != "${sgn_prev}" ]]; then
      safe=0
    fi
    if [[ ${abs_diff} -gt 3 || ${abs_diff} -lt 1 ]]; then
      safe=0
    fi
    # echo "${prev} ${item} ${sgn_prev} ${sgn_diff} ${abs_diff} ${diff}"
    prev=${item}
    sgn_prev=${sgn_diff}
  done
  echo "${safe}"
}

function count_safe() {
  local sum=0
  for l1 in "${dec02_input[@]}"; do
    ((sum+=$(is_safe "${l1}")))
  done
  echo "${sum}"
}

function dec02_test() {
    # Part 1
    dec02_input=("7 6 4 2 1" "1 2 7 8 9" "9 7 6 2 1" "1 3 2 4 5" "8 6 4 4 1" "1 3 6 7 9")
    (( $(count_safe) == 2)) || return 1

    # Part 2
    #(( $(similarity_score) == 31)) || return 1
    #return 0
}

function dec02_main() {
    declare -a dec02_input
    read_file_to_arr 2024 2 dec02_input

    echo "Part 1: $(count_safe)"
    #echo "Part 2: $(similarity_score)"
}

if [ "$1" == "test" ]; then
    dec02_test
else
    dec02_main
fi