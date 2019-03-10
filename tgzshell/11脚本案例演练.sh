#!/bin/bash

#定义本地变量,接受脚本传参
a="$1"

# 编写脚本帮助信息
func(){
	echo ":脚本使用方式 $0 [ start|stop|restart ]"
}

#脚本主框架
 if [[ "$#" -eq 1 ]]; then
 	case "${a}" in
 		start)
			echo "启动...."
 			;;
 		stop)
			echo "关闭..."
			;;
		restart)
			echo "重启...."
			;;
		*)
			func
			;;
 	esac

 else
 	
 	func
 fi