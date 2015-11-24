#!/bin/bash

source ../conf/conf.sh $1
source ../lib/util.sh

echo "Current shitu type is ${shitu_type}"
if ((shitu_type == "wise"))
then
	base_ue_path=${base_ue_wise_path}
elif ((shitu_type == "pc"))
then
	base_ue_path=${base_ue_pc_path}
fi

echo "Checking validation of path..."
input_path=""
for month in ${months[@]}
do
	for date in ${dates[@]}
	do
		cur_path="${base_ue_path}${year}${month}${date}"
		check_valid_path ${cur_path}
		if [ $? -eq 0 ]
		then
			input_path="${input_path} ${cur_path}/part-*"
		fi
	done
done
echo "Input paths are: ${input_path}"


echo "Checking existence of path..."
check_exist_path ${output_path}
if [ $? -ne 0 ]
then
	exit 1
fi

${HADOOP} streaming \
	-D stream.map.output.field.separator="\t" \
	-D stream.num.map.output.key.fields=3 \
	-D map.output.key.field.separator="\t" \
	-D num.key.fields.for.partition=3 \
	-D mapred.reduce.tasks=${statistic_reduce_task_num} \
	-D mapred.combine.input.format.local.only=false \
	-D mapred.min.split.size=${min_split_size} \
	-D mapred.job.map.capacity=${num_map_capacity} \
	-D mapred.job.reduce.capacity=${num_reduce_capacity} \
	-inputformat "org.apache.hadoop.mapred.CombineTextInputFormat" \
	-input ${input_path} \
	-output ${output_path} \
	-mapper "python mapper.get_medical_bid_click.py ${shitu_type}" \
	-reducer "python reducer.sum_average_bid_click.py" \
	-file "../lib/Filter.so" \
	-file "mapper.get_medical_bid_click.py" \
	-file "reducer.sum_average_bid_click.py"

ret_inter=$?
if [ ${ret_inter} -ne 0 ]
then	
	echo "Error! Hadoop Streaming Job was Failed."
	exit 1
else
	echo "Hadoop Streaming Job was successful!" 
fi
