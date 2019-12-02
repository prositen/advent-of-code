source ../common.bash

function jump_offsets() {
  local exit=${#dec05_input[@]}
  local pc=0
  local steps=0
  while true; do
    if (( (pc >= exit) || (pc < 0) )); then
      echo "${steps}"
      return
    fi
    local current=${dec05_input[pc]}
    if [ "$1" == "part2" ]; then
      if (( current >= 3 )); then
        ((dec05_input[pc] -= 1))
      else
        ((dec05_input[pc] += 1))
      fi
    else
      ((dec05_input[pc] += 1))
    fi
    ((pc += current))
    ((steps += 1))
  done
}

function dec05_test() {
  dec05_input=("0" "3" "0" "1" "-3")
  (( $(jump_offsets part1) == 5)) || return 1
  dec05_input=("0" "3" "0" "1" "-3")
  (( $(jump_offsets part2) == 10)) || return 1
  return 0
}


function dec05_main() {
  declare -a dec05_input
  read_file_to_arr 2017 5 dec05_input
  echo "Part 1: $(jump_offsets)"
}


if [ "x$1" == "xtest" ]; then
    dec05_test
else
    dec05_main
fi