#!/bin/bash

date=$1
time=$2
task_id=$3
# khan hadoop path.
HADOOP="/home/work/hadoop-client-khan/hadoop/bin/hadoop"

# Path of bidword & url information.
bid_info_path="/app/ecom/fcr/adw/biddump/${date}/${time}/"
# Path of output of first step,
# which contains winfoid, bidword and url.
output_word_url_winfoid_path="/app/ecom/fcr/zhuxin01/zhushixiang/query_url_relevance_q/word_url_winfoid/"
output_word_url_path="/app/ecom/fcr/zhuxin01/zhushixiang/query_url_relevance_q/word_url/"
# Path of query url relevance q platform.
query_url_predict_path="/app/ecom/fcr/qlq_predict/query_url/${task_id}/"
query_url_relevance_q_platform_path="/app/ecom/fcr/qlq_predict/task/"
query_url_relevance_q_result_path="/app/ecom/fcr/qlq_predict/query_url_q/${task_id}/"
query_url_history_task_path="/app/ecom/fcr/qlq_predict/history_task/"
# Path of result,
# which is joint by output_word_url and query_url_relevance_q_result
relevance_q_path="/app/ecom/fcr/zhuxin01/zhushixiang/query_url_relevance_q/relevance_q/"
result_path="/app/ecom/fcr/zhuxin01/zhushixiang/query_url_relevance_q/result/"

# Essential Parameter.
normal_reduce_tasks_num=100
statistic_reduce_task_num=1
min_split_size=100000000
num_map_capacity=1000
num_reduce_capacity=1000
