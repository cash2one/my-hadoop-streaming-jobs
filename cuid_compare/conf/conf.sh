#!/bin/bash

# Source of data which need to be processed later.
base_path="/app/ecom/fcr-important/shitu-log-wise/222_223"
input_path=""

# Destination of result.
output_path="/app/ecom/fcr-ad/zhushixiang/cuid_compare"

# Essential Parameter.
normal_reduce_tasks_num=100
statistic_reduce_task_num=1
min_split_size=100000000
num_map_capacity=1000
num_reduce_capacity=1000
