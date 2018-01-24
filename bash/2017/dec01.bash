#!/bin/bash
source ./common.bash


function captcha() {
	local input=$1
	local input_length="${#input}"
	local value
	local prev_value
	local sum
	local step
	if [ "$2" == "part1" ]; then
		step=1
	else
		step=$((input_length / 2))
	fi
	for (( i=0; i< $input_length; i++ )); do
		compare_pos=$((i+step))
		if (( $compare_pos >= $input_length )); then
			compare_pos=$((compare_pos - input_length))
		fi
		cur_value="${input:$i:1}"
		compare_value="${input:$compare_pos:1}"
		if [ "$cur_value" == "$compare_value" ]; then
			sum="$((sum + cur_value))"
		fi
	done
	echo "$sum"
}


value=$(read_file_to_var 2017 1)
echo "Part 1: $(captcha $value part1)"
echo "Part 2: $(captcha $value part2)"
