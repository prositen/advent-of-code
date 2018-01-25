#!/bin/bash

##
# value=$(read_file_to_var year day)
##
function read_file_to_var() {
	local year=$1
	local day=$2
	local value=$(<../../data/${year}/input.${day}.txt)
	echo ${value}
}

##
# read_file_to_array year day value
##
function read_file_to_arr() {
    # array keys: ${!array[@]}
    local year=$1
    local day=$2
    readarray -t "$3" < ../../data/${year}/input.${day}.txt
}

function sort_arr() {
    local output=$1
    shift
    local sort_arr_IN
    read -r -a sort_arr_IN <<< "$@"

    local sort_arr_OUT
    IFS=$'\n' sort_arr_OUT=($(sort -n <<< "${sort_arr_IN[*]}"))
    unset IFS
    read -r -a "$output" <<< "${sort_arr_OUT[*]}"
}

