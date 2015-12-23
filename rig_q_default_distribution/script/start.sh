#!/bin/bash
source ../conf/conf.sh
source ../lib/util.sh

echo_info "Checking validation of input path"
input_path=""
date_array=(`echo ${dates} | awk 'BEGIN{ FS=",";OFS=" " }{$1=$1;print}'`)
date_num=${#date_array[@]}
for date in ${date_array[@]}
do
	check_valid_path "${input_base_path}/${date}"
	if [ $? -ne 0 ]
	then
		echo_error "Invalid input path."
		exit 1
	else
		input_path="${input_path} ${input_base_path}/${date}/*/part-*"
	fi
done
echo_info "Input path are: ${input_path}"

echo_info "Checking existence of output path..."
output_path="${output_base_path}/${dates}"
check_exist_path ${output_path}
if [ $? -ne 0 ]
then
	echo_error "Error occurs when checking existence of output path."
	exit 1
fi

echo_info "Hadoop Streaming job started."
${HADOOP} streaming \
	-D mapred.job.name="${owner_tag}.${task_tag}" \
	-D mapred.reduce.tasks=${reduce_task_num} \
	-D mapred.combine.input.format.local.only=false \
	-D mapred.min.split.size=${min_split_size} \
	-D mapred.job.map.capacity=${num_map_capacity} \
	-D mapred.job.reduce.capacity=${num_reduce_capacity} \
	-D mapred.job.priority="${job_priority}" \
	-partitioner "org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner" \
	-inputformat "org.apache.hadoop.mapred.CombineTextInputFormat" \
	-input ${input_path} \
	-output ${output_path} \
	-mapper "python mapper.get_count.py" \
	-reducer "python reducer.merge_count.py" \
	-file "mapper.get_count.py" \
	-file "reducer.merge_count.py"

ret_inter=$?
if [ ${ret_inter} -ne 0 ]
then	
	echo_error "Error! Hadoop Streaming Job was Failed."
	exit 1
else
	echo_info "Hadoop Streaming Job was successful!" 
fi

check_do "sh output_result.sh"
