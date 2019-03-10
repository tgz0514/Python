#!/bin/bash
# case语句使用场景
#定义一个本地变量,接受脚本传入的参数
a="$1"

case "${a}" in
	start)
		echo "启动....." 
			;;
	stop)
		echo "关闭...."
			;;
	restart)
		echo "重启"
		;;
	*)
		echo "$0 脚本的使用方式： $0 [ start | stop | restart ]"
		;;
esac