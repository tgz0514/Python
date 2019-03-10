#!/bin/bash

a="$1"

if [ "${a}" == "nan" ]
then
    echo "男"
elif [ "${a}" == "nv" ]
then
   echo "女"
else
    echo "未知"
fi

