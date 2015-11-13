#!/bin/bash

date=$1
time=$2
task_id=$3

source ../conf/conf.sh ${date} ${time} ${task_id}

${HADOOP} fs -mv ${query_url_relevance_q_result_path}* ${relevance_q_path}
ret=$?
if [ ${ret} -ne 0 ]
then
	echo "Error! Moving relevance file to local hadoop was failed."
	exit 1
fi
echo "Move relevance file to local hadoop successfully."

${HADOOP} fs -rmr ${relevance_q_path}done
ret=$?
if [ ${ret} -ne 0 ]
then
	echo "Error! Removing done file in hadoop successfully."
	exit 1
fi
echo "Remove done file in hadoop successfully."

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
	-input ${relevance_q_path} \
	-input ${output_word_url_winfoid_path} \
	-output ${result_path} \
	-mapper "python mapper.tag.py" \
	-reducer "python reducer.join.py" \
	-file "mapper.tag.py" \
	-file "reducer.join.py"
