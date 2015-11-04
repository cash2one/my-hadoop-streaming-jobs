#!/bin/bash
# Author@		Woodie
# UpdatedAt@	Wed, Nov 4, 2015

# Validation of number of input parameters
# if [ $# -ne 4 ]
# then
# 	echo "Error! The number of input parameters was wrong. 4 was expected, but there is $#."
# 	exit 1
# fi

source ../conf/conf.sh

# Validation of existence of input path.
for date in $@
do
	# Validation of existence of directory.
	echo "Directory of ${base_path}/${date} is being checked..."
	if hadoop fs -test -e ${base_path}/${date}
	then
		echo "The check was passed."
		# Join the new input path.
		input_path="${input_path} ${base_path}/${date}/*/part-*"
	else
		echo "Error! The path is not existed. Please check it."
		exit 1
	fi
done
echo "The input path for hadoop streaming is: ${input_path}"

# Validation of existence of output path and Removing the path which was existed.
if hadoop fs -test -e ${output_path}
then
	echo "Warning! The output path ${output_path} is existed. Removing..."
	hadoop fs -rmr ${output_path}
	if [ $? -ne 0 ]
	then 
		echo "Error! ${output_path} was failed to remove."
		exit 1
	fi
fi
echo "The output path for hadoop streaming is: ${output_path}"

# Hadoop Streaming Job:
# - Map: extract winfoid and date as mutiple key. Results were sorted by both of them
# - Reduce: get the difference section and intersection of set A(data of today) and set B(data of yesterday) 
hadoop streaming \
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
	-input ${input_path} \
	-output ${output_path} \
	-mapper "python mapper.slot_cuid_cmatch.py" \
	-reducer "python reducer.statistics.py" \
	-file "mapper.slot_cuid_cmatch.py" \
	-file "reducer.statistics.py"
	
ret=$?
if [ ${ret} -ne 0 ]
then	
	echo "Error! Hadoop Streaming Job was Failed."
	exit 1
else
	echo "Hadoop Streaming Job was successful!" 
	exit 0
fi