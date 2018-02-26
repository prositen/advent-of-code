#!/usr/bin/env bash
source ./common.bash
function high_entropy_passphrases() {
    local valid_passphrases=0
    local uniq
    for i1 in ${!dec04_input[@]}; do
        local phrase
        read -r -a phrase <<< "${dec04_input[i1]}"
        local len_passphrase="${#phrase[@]}"
        uniq_arr uniq "${dec04_input[i1]}"
        local len_uniq=${#uniq[@]}
        if ((len_uniq == len_passphrase)); then
            ((valid_passphrases+=1))
        fi
    done
    echo "${valid_passphrases}"

}
function dec04_test() {
    dec04_input=("aa bb cc dd ee" "aa bb cc dd aa" "aa bb cc dd aaa")
    (( $(high_entropy_passphrases) == 2)) || return 1
    return 0
}
function dec04_main() {
    declare -a dec04_input
    read_file_to_arr 2017 4 dec04_input
    echo "Part 1: $(high_entropy_passphrases)"
}

if [ "x$1" == "xtest" ]; then
    dec04_test
else
    dec04_main
fi