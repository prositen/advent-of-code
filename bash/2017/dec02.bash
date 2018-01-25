#!/usr/bin/env bash

source ./common.bash
declare -a dec02_input
read_file_to_arr 2017 2 dec02_input


function corruption_checksum() {
    local checksum=0
    local sorted
    for i1 in ${!dec02_input[@]}; do
        sort_arr sorted "${dec02_input[i1]}"
        local len=${#sorted[@]}
        checksum="$((checksum + sorted[$len-1] - sorted[0]))"
    done
    echo ${checksum}
}

function even_divisble_checksum() {
    local checksum=0
    for i1 in ${!dec02_input[@]}; do
        local line
        read -r -a line <<< ${dec02_input[i1]}
        for i2 in "${!line[@]}"; do
            local a=${line[$i2]}
            local found=0
            for i3 in "${!line[@]}"; do
                if (( $i3 > $i2 )); then
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
            if (( $found > 0)); then
                ((checksum += found))
                break
            fi
        done
    done
    echo ${checksum}
}


echo "Part 1: $(corruption_checksum)"
echo "Part 2: $(even_divisble_checksum)"


