#!/bin/bash

export HADOOP="/home/work/hadoop-client/hadoop/bin/hadoop"

# Input base path & sub path
export input_base_path="/app/ecom/fcr-important/shitu-log-wise/222_223"
export output_base_path="/app/ecom/fcr-ad/zhushixiang/rig_q_default_ratio"
export dates="20151221"
# Basic config 
export owner_tag="zhushixiang"
export task_tag="rigq_default_ratio_20151221"
export created_at=`date +%Y%m%d-%H%M%S`
# Hadoop parameter
export reduce_task_num=1
export min_split_size=100000000
export num_map_capacity=1000
export num_reduce_capacity=1000
#export job_priority="NORMAL"
export job_priority="VERY_HIGH"
