#!/bin/bash

function check_valid_path
{
	__path=$@
	if ${HADOOP} fs -test -e ${__path}
	then
		echo "Path ${__path} is valid."
		return 0
	else
		echo "Warning! Path ${__path} is invalid!"
		return 1
	fi
}

function check_exist_path
{
	__path=$@
	if ${HADOOP} fs -test -e ${__path}
	then
		echo "Warning! Path ${__path} is existed!"
		${HADOOP} fs -rmr ${__path}
		if [ $? -ne 0 ]
		then
			echo "FATAL, ${__path} removed failed."
			return 1
		else
			echo "${__path} was removed successfully."
			return 0
		fi
	fi
}
