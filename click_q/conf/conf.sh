#!/bin/bash

# Initiation of variable

#
# - Source of Data
#
input_path=""
root_dir="/app/ecom/fcr-ad/wubo01/dps/base_ue/"
for date in $@
do
	# Validation of existence of directory.
	echo "Directory of ${root_dir}${date} is being checked..."
	hadoop fs -test -e ${root_dir}${date}
	if [ $? -ne 0 ]
	then
		echo "Error! The path is not existed. Please check it."
		exit 1
	fi
	echo "The check was passed."
	# Join the new input path.
	input_path="${input_path} ${root_dir}${date}/part-*"
done
echo "The input path for hadoop streaming is: ${input_path}"

#
# - Destination of result.
#
output_path="/app/ecom/fcr-ad/zhushixiang/click_q"
echo "Directory of ${output_path} is being checked..."
hadoop fs -test -e ${output_path}
if [ $? -ne 0 ]
then
	echo "Error! The path is not existed. Please check it."
	exit 1
fi
echo "The check was passed."
echo "The output path for hadoop streaming is: ${output_path}"

#
# - Essential Parameter.
#
statistic_reduce_task_num=8
min_split_size=100000000
num_map_capacity=1000
num_reduce_capacity=1000
