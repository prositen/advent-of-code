#!/bin/bash

for day in 01 02 03 04; do
    echo "2017-12-${day}"
    source ./dec${day}.bash test  && echo "Ok" || exit 1
done

