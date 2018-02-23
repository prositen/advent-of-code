#!/bin/bash
source ./common.bash

dec03_input="325489"


function spiral_step() {
    local input=$1
    local part=$2
    local steps=1
    local x=0
    local y=0
    local dir_x=1
    local dir_y=0
    local value=1
    while true; do
        local side
        for side in 1 2; do
            local step=0
            while [ ${step} -lt ${steps} ]; do
                if [ ${value} -ge ${input} ]; then
                    x=$(abs ${x})
                    y=$(abs ${y})
                    ((steps=x+y))
                    echo "${steps}"
                    return
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



echo "Part 1: $(spiral_step ${dec03_input} part1)"
# echo "Part 2: $(spiral_step ${dec03_input} part2)"