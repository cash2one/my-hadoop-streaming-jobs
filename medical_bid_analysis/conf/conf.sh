#!/bin/bash
shitu_type=$1

export HADOOP="/home/work/hadoop-client/hadoop/bin/hadoop"

year="2015"
dates=("02" "03" "04" "05" "06" "07" "08" "09" "10" "13" "14" "15" "16" "17" "18" "19" "20" "21" "22" "23" "24" "25" "26" "27" "28")
base_ue_pc_path="/app/ecom/fcr-ad/wubo01/dps/base_ue/"
base_ue_wise_path="/app/ecom/fcr/fcr-public/wubo01/wiseclkdata_base_ue/"

base_medical_path="/app/ecom/fcr-ad/zhushixiang/medical_bid/bidword_key/fix_control/"
#base_medical_path="/app/ecom/fcr-ad/zhushixiang/medical_bid/bidword_key/near_control/"
bidword_domain_path="/app/ecom/fcr-ad/zhushixiang/medical_bid/bidword_key/near_control/raw_data/"
intersection_path="${base_medical_path}intersection/"
meta_result_path="${base_medical_path}meta_result/"
experimental_list=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10")
control_list=("11" "11" "11" "11" "11" "11" "11" "11" "11" "11")
#control_list=("02" "03" "04" "05" "06" "07" "08" "09" "10" "11")
#
# - Essential Parameter.
#
step_1_reduce_task_num=100
step_2_reduce_task_num=20
step_3_reduce_task_num=1
min_split_size=100000000
num_map_capacity=1000
num_reduce_capacity=1000

owner_name="zhushixiang"
job_priority="VERY_HIGH"
#job_priority="NORMAL"
