#!/bin/bash

date=$1
time=$2
task_id=$3

source ../conf/conf.sh ${date} ${time} ${task_id}

step1_input_path=""
echo "Directory of ${bid_info_path} is being checked..."
if ${HADOOP} fs -test -e ${bid_info_path}
then
	echo "The check was passed."
	# Join the new input path.
	step1_input_path="${bid_info_path}/bid.info_*"
else
	echo "Error! The path is not existed. Please check it."
	exit 1
fi
echo "The First step input path is: ${step1_input_path}"

echo "Directory of ${output_word_url_path} is being checked..."
if ${HADOOP} fs -test -e ${output_word_url_path}
then
	echo "Warning! The output path ${output_word_url_path} is existed. Removing..."
	hadoop fs -rmr ${output_word_url_path}
	if [ $? -ne 0 ]
	then 
		echo "Error! ${output_word_url_path} was failed to remove."
		exit 1
	fi
fi
echo "The First step output path is: ${output_word_url_path}"

echo "Directory of ${output_word_url_winfoid_path} is being checked..."
if ${HADOOP} fs -test -e ${output_word_url_winfoid_path}
then
	echo "Warning! The output path ${output_word_url_winfoid_path} is existed. Removing..."
	hadoop fs -rmr ${output_word_url_winfoid_path}
	if [ $? -ne 0 ]
	then 
		echo "Error! ${output_word_url_winfoid_path} was failed to remove."
		exit 1
	fi
fi
echo "The First step output path is: ${output_word_url_winfoid_path}"

# Data 1
${HADOOP} streaming \
	-D stream.map.output.field.separator="\t" \
	-D stream.num.map.output.key.fields=2 \
	-D map.output.key.field.separator="\t" \
	-D num.key.fields.for.partition=2 \
	-D mapred.reduce.tasks=${statistic_reduce_task_num} \
	-D mapred.combine.input.format.local.only=false \
	-D mapred.min.split.size=${min_split_size} \
	-D mapred.job.map.capacity=${num_map_capacity} \
	-D mapred.job.reduce.capacity=${num_reduce_capacity} \
	-inputformat "org.apache.hadoop.mapred.CombineTextInputFormat" \
	-input ${step1_input_path} \
	-output ${output_word_url_path} \
	-mapper "python mapper.get_word_url.py" \
	-file "mapper.get_word_url.py"
	-file "../lib/url_util.py"
	
ret=$?
if [ ${ret} -ne 0 ]
then
	echo "Error! Hadoop Streaming Job was Failed."
	exit 1
fi

# Data 2
${HADOOP} streaming \
	-D stream.map.output.field.separator="\t" \
	-D stream.num.map.output.key.fields=2 \
	-D map.output.key.field.separator="\t" \
	-D num.key.fields.for.partition=2 \
	-D mapred.reduce.tasks=${statistic_reduce_task_num} \
	-D mapred.combine.input.format.local.only=false \
	-D mapred.min.split.size=${min_split_size} \
	-D mapred.job.map.capacity=${num_map_capacity} \
	-D mapred.job.reduce.capacity=${num_reduce_capacity} \
	-inputformat "org.apache.hadoop.mapred.CombineTextInputFormat" \
	-input ${step1_input_path} \
	-output ${output_word_url_winfoid_path} \
	-mapper "python mapper.get_word_url_winfoid.py" \
	-file "mapper.get_word_url_winfoid.py"
	-file "../lib/url_util.py"
	
ret=$?
if [ ${ret} -ne 0 ]
then
	echo "Error! Hadoop Streaming Job was Failed."
	exit 1
fi

cp ../resource/task_template ./${task_id}.task

echo "File: ${query_url_history_task_path}${task_id}.task is being checked..."
if ${HADOOP} fs -test -e ${query_url_history_task_path}${task_id}.task
then
	echo "Error! The task file is existed. Please check it."
	exit 1
fi

${HADOOP} fs -put ./${task_id}.task ${query_url_relevance_q_platform_path}
ret=$?
if [ ${ret} -ne 0 ]
then
	echo "Error! Moving task file to hadoop was failed."
	exit 1
fi

${HADOOP} fs -touchz ${query_url_relevance_q_platform_path}${task_id}.done
ret=$?
if [ ${ret} -ne 0 ]
then
	echo "Error! Touching done file in hadoop was failed."
	exit 1
fi