#!/usr/bin/env bash
source ../common.bash

function frequency_change() {
    local sum=0
    for i1 in "${!dec01_input[@]}"; do
        local term=${dec01_input[$i1]}
        ((sum = sum + term))
    done
    echo ${sum}
}


function first_repeating_frequency() {
    declare -A freqs
    local sum=0
    freqs[${sum}]=1
    for (( ; ; ${#freqs[@]} > 10000000))
    do
        for i1 in "${!dec01_input[@]}"; do
            local term=${dec01_input[$i1]}
            ((sum = sum + term))
            if [ -n "${freqs[${sum}]}" ];
            then
                echo ${sum}
                return
            fi
            freqs[${sum}]=1
        done
    done
    echo "Error"
}

function dec01_test() {
    dec01_input=("+1" "-2" "+3" "+1")
    (( $(frequency_change) == 3 )) || return 1

    dec01_input=("+1" "+1" "+1")
    (( $(frequency_change) == 3 )) || return 1

    dec01_input=("+1" "+1" "-2")
    (( $(frequency_change) == 0 )) || return 1

    dec01_input=("-1" "-2" "-3")
    (( $(frequency_change) == -6 )) || return 1

    dec01_input=("+1" "-1")
    (( $(first_repeating_frequency) == 0 )) || return 1

    dec01_input=("+3" "+3" "+4" "-2" "-4")
    (( $(first_repeating_frequency) == 10 )) || return 1

    dec01_input=("-6" "+3" "+8" "+5" "-6")
    (( $(first_repeating_frequency) == 5)) || return 1

    dec01_input=("+7" "+7" "-2" "-7" "-4")
    (( $(first_repeating_frequency) == 14 )) || return 1
}

function dec01_main() {
    declare -a dec01_input
    read_file_to_arr 2018 1 dec01_input
    echo "Part 1: $(frequency_change)"
    echo "Part 2: $(first_repeating_frequency)"

}

if [ "x$1" == "xtest" ]; then
    dec01_test
else
    dec01_main
fi
