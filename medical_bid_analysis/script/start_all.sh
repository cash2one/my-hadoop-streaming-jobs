#!/bin/bash

source ../lib/util.sh

cwd=`pwd`
_date=`date +%Y%m%d`

#check_do "sh bat.get_bidword_domain.sh wise > ../log/all.bidword_domain.${_date}.log"

check_do "sh bat.join.sh wise > ../log/all.join.${_date}.log"

check_do "sh bat.meta.sh wise > ../log/all.meta.${_date}.log"
