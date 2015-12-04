#!/bin/bash

if [ $# \< 3 ]
then
	echo "Error! Parameters are invalid!"
	exit 1
fi

source ../conf/conf.sh $1
source ../lib/util.sh

experimental_group=$2
control_group=$3

echo "Current shitu type is ${shitu_type}"

echo "Checking validation of input path..."
input_path=""
experimental_path=${bidword_domain_path}${shitu_type}/${experimental_group}
control_path=${bidword_domain_path}${shitu_type}/${control_group}
check_valid_path ${experimental_path}
if [ $? -eq 0 ]
then
	input_path="${input_path} ${experimental_path}/part-*"
fi
check_valid_path ${control_path}
if [ $? -eq 0 ]
then
	input_path="${input_path} ${control_path}/part-*"
fi
echo "Input paths are: ${input_path}"

echo "Checking existence of output path..."
output_path="${intersection_path}${shitu_type}/e${experimental_group}-c${control_group}"
check_exist_path ${output_path}
if [ $? -ne 0 ]
then
	exit 1
fi

${HADOOP} streaming \
	-D mapred.job.name="${owner_name}.join" \
	-D stream.map.output.field.separator="\t" \
	-D stream.num.map.output.key.fields=2 \
	-D map.output.key.field.separator="\t" \
	-D num.key.fields.for.partition=1 \
	-D mapred.reduce.tasks=${step_2_reduce_task_num} \
	-D mapred.combine.input.format.local.only=false \
	-D mapred.min.split.size=${min_split_size} \
	-D mapred.job.map.capacity=${num_map_capacity} \
	-D mapred.job.reduce.capacity=${num_reduce_capacity} \
	-D mapred.job.priority="${job_priority}" \
	-inputformat "org.apache.hadoop.mapred.CombineTextInputFormat" \
	-input ${input_path} \
	-output ${output_path} \
	-mapper "python mapper.count_filter.py 5 ${experimental_group} ${control_group}" \
	-reducer "python reducer.join_bidword_domain.py" \
	-file "mapper.count_filter.py" \
	-file "reducer.join_bidword_domain.py"

ret_inter=$?
if [ ${ret_inter} -ne 0 ]
then	
	echo "Error! Hadoop Streaming Job was Failed."
	exit 1
else
	echo "Hadoop Streaming Job was successful!" 
fi
