#!/usr/bin/env bash

source ../common.bash


function corruption_checksum() {
    local checksum=0
    local sorted
    for i1 in "${!dec02_input[@]}"; do
        sort_arr sorted "${dec02_input[i1]}"
        local len=${#sorted[@]}
        checksum="$((checksum + sorted[len-1] - sorted[0]))"
    done
    echo ${checksum}
}

function even_divisible_checksum() {
    local checksum=0
    for i1 in "${!dec02_input[@]}"; do
        local line
        read -r -a line <<< "${dec02_input[i1]}"
        for i2 in "${!line[@]}"; do
            local a=${line[$i2]}
            local found=0
            for i3 in "${!line[@]}"; do
                if (( i3 > i2 )); then
                    local b=${line[$i3]}
                    if (( (a % b) == 0 )); then
                        ((found = a / b))
                        break
                    elif (( (b % a) == 0)); then
                        ((found = b / a))
                        break
                    fi
                fi
            done
            if (( found > 0)); then
                ((checksum += found))
                break
            fi
        done
    done
    echo "${checksum}"
}


function dec02_test() {
    dec02_input=("5 1   9   5" "7   5   3"  "2  4   6   8")
    (( $(corruption_checksum) == 18 )) || return 1

    dec02_input=("5 9   2   8" "9   4   7   3" "3   8   6   5")
    (( $(even_divisible_checksum) == 9)) || return 1

}

function dec02_main() {
    declare -a dec02_input
    read_file_to_arr 2017 2 dec02_input

    echo "Part 1: $(corruption_checksum)"
    echo "Part 2: $(even_divisible_checksum)"
}


if [ "x$1" == "xtest" ]; then
    dec02_test
else
    dec02_main
fi
