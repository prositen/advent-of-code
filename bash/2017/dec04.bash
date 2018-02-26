#!/usr/bin/env bash
source ./common.bash
function high_entropy_passphrases() {
    local valid_passphrases=0
    local uniq
    for i1 in ${!dec04_input[@]}; do
        local phrase
        read -r -a phrase <<< ${dec04_input[i1]}
        if [ "$1" == "part2" ]; then
            local sorted_phrase=()
            for p1 in ${!phrase[@]}; do
                sorted_phrase+=($(sort_letters ${phrase[p1]}))
            done
            read -r -a phrase <<< "${sorted_phrase[@]}"
        fi
        local len_passphrase="${#phrase[@]}"
        uniq_arr uniq "${phrase[@]}"
        local len_uniq=${#uniq[@]}
        if ((len_uniq == len_passphrase)); then
            ((valid_passphrases+=1))
        fi
    done
    echo "${valid_passphrases}"
}

function dec04_test() {
    dec04_input=("aa bb cc dd ee" "aa bb cc dd aa" "aa bb cc dd aaa")
    (( $(high_entropy_passphrases part1) == 2)) || return 1
    dec04_input=("abcde fghij" "abcde xyz ecdab" "a ab abc abd abf abj" "iiii oiii ooii oooi oooo" "oiii ioii iioi iiio")
    (( $(high_entropy_passphrases part2) == 3)) || return 1
    return 0
}

function dec04_main() {
    declare -a dec04_input
    read_file_to_arr 2017 4 dec04_input
    echo "Part 1: $(high_entropy_passphrases part1)"
    echo "Part 1: $(high_entropy_passphrases part2)"
}

if [ "x$1" == "xtest" ]; then
    dec04_test
else
    dec04_main
fi