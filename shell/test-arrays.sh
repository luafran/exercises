#!/bin/bash

array_contains ()
{
    local array="$1[@]"
    local seeking=$2
    local in=0
    
    for element in "${!array}"; do
        if [[ $element == $seeking ]]; then
            in=1
            break
        fi
    done
    
    return $in
}

command1 ()
{
    echo "command 1"
}


command2 ()
{
    echo "command 2"
}


command3 ()
{
    echo "command 3"
}

VALID_COMMANDS=(command1 command2 command3)

command=$1

array_contains VALID_COMMANDS ${command}
res=$?
if [ $res == 0 ]; then
    echo "ERROR: Unknown command: ${command}"
    echo "Valid commands: ${VALID_COMMANDS[@]}"
    exit 1
fi

eval ${command}

