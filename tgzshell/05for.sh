#!bin/bash
# for循环的使用案例

for i in $(ls .)
do
	echo ". 目录下面有文件: ${i}"
done