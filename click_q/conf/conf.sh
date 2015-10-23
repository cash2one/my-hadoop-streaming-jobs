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
	if hadoop fs -test -e ${root_dir}${date}
	then
		echo "The check was passed."
		# Join the new input path.
		input_path="${input_path} ${root_dir}${date}/part-*"
	else
		echo "Error! The path is not existed. Please check it."	
	fi
done
echo "The input path for hadoop streaming is: ${input_path}"

#
# - Destination of result.
#
output_path="/app/ecom/fcr-ad/zhushixiang/click_q"
echo "Directory of ${output_path} is being checked..."
if hadoop fs -test -e ${output_path}
then
	echo "Warning! The output path ${output_path} is existed. Removing..."
	hadoop fs -rmr ${output_path}
fi
echo "The check was passed."
echo "The output path for hadoop streaming is: ${output_path}"

#
# - Essential Parameter.
#
statistic_reduce_task_num=1
min_split_size=100000000
num_map_capacity=1000
num_reduce_capacity=1000
