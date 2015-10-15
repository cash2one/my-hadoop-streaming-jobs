#!/bin/bash
# Author@		Woodie
# UpdatedAt@	Thu, Oct 8, 2015
# Usage@		nohup sh ./start.sh [param1] [param2] [param3] [param4] > ../log/timestamp.log &
#				- param1: today's data sub-directory, eg: 20151002
#				- param2: yesterday's data sub-directory, eg: 20151001
#				- param3: today's date, eg: 2
#				- param4: yesterday's date, eg: 1
# Description@	The first two parameters are used to locate the input data. And the last two parameters are used to tell the reducer about the date of today and yester. This method is dirty but easy to use and efficient. You should ensure the dates of today and yesterday is the dates which param1 and param2 contain.

source ../conf/conf.sh $@

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
	-mapper "python mapper.get_click.py 20150922_cn_dict.txt" \
	-reducer "python reducer.click_q.py" \
	-file "../resource/20150922_cn_dict.txt" \
	-file "../lib/utils.py" \
	-file "mapper.get_click.py" \
	-file "reducer.click_q.py"
ret_inter=$?
if [ ${ret_inter} -ne 0 ]
then	
	echo "Error! Hadoop Streaming Job of ClickQ was Failed."
	exit 1
else
	echo "Hadoop Streaming Job of ClickQ was successful!" 
fi
