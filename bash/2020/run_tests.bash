#!/bin/bash

for day in 01; do
    echo "2020-12-${day}"
    source ./dec${day}.bash test  && echo "Ok" || exit 1
done

