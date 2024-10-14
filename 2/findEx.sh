#!/bin/bash
function printPath(){
    home = $(echo $HOME)
    length = ${#home}
    if [ "${$1:0:10}" = $home ]
    then
        echo "~${$1:$length}"
    else
        echo $1
    fi
}
function getdir(){
    for ele in `ls $1`
    do  
        dir_or_file=$1"/"$ele
        if [ -d $dir_or_file ]
        # is dir
        then 
            getdir $dir_or_file $2
        else
            if [ "${dir_or_file##*.}"x = "$2"x ]
            then
                printPath $dir_or_file
            fi
        fi
    done
}

while true
do
    read -p "Please input file extension (q to quit):" file_ex

    if [ $file_ex == "q" ]
    then
        exit
    fi
    read -p "Please input directory to search (q to quit):" dir_name
    if [ $dir_name == "q" ]
    then
        exit
    fi

    getdir $dir_name $file_ex
done