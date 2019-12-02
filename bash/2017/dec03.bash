#!/bin/bash
source ../common.bash




function spiral_step() {
    local input=$1
    local part=$2
    local steps=1
    local x=0
    local y=0
    local dir_x=1
    local dir_y=0
    local value=1
    local m
    declare -A m
    m[0,0]=1
    while true; do
        for side in 1 2; do
            local step=0
            while [ ${step} -lt ${steps} ]; do
                if [ "$part" == "part2" ]; then
                    local r_0=$((m[$((x-1)),$((y-1))] + m[$((x-1)),$y] + m[$((x-1)),$((y+1))]))
                    local r_1=$((m[$x,$((y-1))]       + m[$x,$y]       + m[$x,$((y+1))]))
                    local r_2=$((m[$((x+1)),$((y-1))] + m[$((x+1)),$y] + m[$((x+1)),$((y+1))]))
                    local m0=$((r_0 + r_1 + r_2))
                    if (( m0 > input )); then
                        echo "${m0}"
                        return
                    fi
                    m[${x},${y}]=${m0}
                fi
                if (( value >= input )); then
                    if [ "$part" == "part1" ]; then
                        x=$(abs ${x})
                        y=$(abs ${y})
                        ((steps=x+y))
                        echo "${steps}"
                        return
                    fi
                fi
                ((x += dir_x))
                ((y += dir_y))
                ((value += 1))
                ((step += 1))
            done
            local tmp_dir=${dir_x}
            ((dir_x=dir_y))
            ((dir_y=-tmp_dir))
        done
        ((steps+=1))
    done
}


function dec03_main() {
    local dec03_input="325489"
    echo "Part 1: $(spiral_step ${dec03_input} part1)"
    echo "Part 2: $(spiral_step ${dec03_input} part2)"

}

function dec03_test() {
    (( $(spiral_step 1 part1) == 0)) \
    && (( $(spiral_step 12 part1) == 3)) \
    && (( $(spiral_step 23 part1) == 2)) \
    && (( $(spiral_step 1024 part1) == 31))  \
    || return 1

    (( $(spiral_step 1 part2) == 2)) \
    && (( $(spiral_step 12 part2) == 23)) \
    && (( $(spiral_step 23 part2) == 25)) \
    && (( $(spiral_step 1024 part2) == 1968)) \
    || return 1

    return 0
}

if [ "x$1" == "xtest" ]; then
    dec03_test
else
    dec03_main
fi
