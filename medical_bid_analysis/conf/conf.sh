#!/bin/bash
shitu_type=$1

export HADOOP="/home/work/hadoop-client/hadoop/bin/hadoop"

year="2015"
months=("09" "10" "11")
dates=("21" "22")
base_ue_pc_path="/app/ecom/fcr-ad/wubo01/dps/base_ue/"
base_ue_wise_path="/app/ecom/fcr/fcr-public/wubo01/wiseclkdata_base_ue/"
output_path="/app/ecom/fcr-ad/zhushixiang/medical_bid_analysis/"
#
# - Essential Parameter.
#
statistic_reduce_task_num=100
min_split_size=100000000
num_map_capacity=1000
num_reduce_capacity=1000
