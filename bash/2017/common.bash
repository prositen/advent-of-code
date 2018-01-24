#!/bin/bash

function read_file_to_var() {
	local year=$1
	local day=$2
	local value=$(<../../data/$year/input.$day.txt)
	echo $value
}
