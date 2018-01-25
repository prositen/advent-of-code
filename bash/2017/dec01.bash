#!/bin/bash
source ./common.bash


function captcha() {
	local input=$1
	local input_length="${#input}"
	local sum=0
	local step=1
	if [ "$2" != "part1" ]; then
		((step = input_length / 2))
	fi
	for (( i=0; i< $input_length; i++ )); do
		((compare_pos = (i+step) % input_length))
		local cur_value="${input:$i:1}"
		local compare_value="${input:$compare_pos:1}"
		if [ "$cur_value" == "$compare_value" ]; then
			(( sum += cur_value))
		fi
	done
	echo "$sum"
}

function dec01_test() {

    # Part 1
    (( $(captcha 1122 part1) == 3 )) \
    &&  (( $(captcha 1111 part1) == 4 )) \
    && (( $(captcha 1234 part1) == 0)) \
    && (( $(captcha 91212129 part1) == 9)) \
    || return 1


    # Part 2
    (( $(captcha 1212 part2) == 6 )) \
    && (( $(captcha 1221 part2) == 0 )) \
    && (( $(captcha 123425 part2) == 4 )) \
    && (( $(captcha 123123 part2) == 12)) \
    && (( $(captcha 12131415 part2) == 4)) \
    || return 1
    return 0
}

function dec01_main() {
    local value=$(read_file_to_var 2017 1)
    echo "Part 1: $(captcha $value part1)"
    echo "Part 2: $(captcha $value part2)"
}

if [ "x$1" == "xtest" ]; then
    dec01_test
else
    dec01_main
fi
