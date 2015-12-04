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

function log
{
    local __msg=$@
    local __prefix=[`date +"%Y-%m-%d %H:%M:%S"`]
    if [ "$LOG_FILE" == "" ] ; then
        echo "${__prefix}${__msg}"
    else
        echo "${__prefix}${__msg}" >>$LOG_FILE
    fi
}

function check_return_value
{
    if [ $? -eq 0 ] ; then
        log "[succ]"
    else
        log "[fail]"
        log "[I will exit, sorry!!!]"
        exit 1
    fi  
}

function check_do
{
    __cmd=$@
    log "${__cmd}"
    ${__cmd}
    check_return_value
}


