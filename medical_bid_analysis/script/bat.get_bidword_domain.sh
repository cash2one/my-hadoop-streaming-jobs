cur_dir=`pwd`
program="start.get_bidword_domain.sh"
shitu_type=$1
batch_list=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10" "11")
batch_size=3

flag="0"
task_num=${#batch_list[@]}
today_date=`date +%Y%m%d`

mkdir ../log/bidword_domain.${today_date}
mkdir ../log/bidword_domain.${today_date}/${shitu_type}

for (( i = 0 ; ; ))
do
	if [ ${flag} -eq 1 ]
	then
		break
	fi

	for (( j = 0; j < batch_size; j ++ ))
	do
		if [ ${i} == ${task_num} ] 
		then
			echo "All batch tasks are finished."
			flag="1"
			break
		fi

		echo "Starting Task ${j}, month = ${batch_list[${i}]}, shitu = ${shitu_type} ..."
		sh ${program} ${shitu_type} ${batch_list[${i}]} > ../log/bidword_domain.${today_date}/${shitu_type}/task.${shitu_type}.month_${batch_list[${i}]}.log 2>&1 &
		pid_pool[${j}]=$!
		sleep 5

		(( i ++ ))
	done

	echo "Current tasks has reached maximum of batch size. Waitting until current tasks all finish."
	echo "PID pool detail as follow:"
	for pid in ${pid_pool[@]}
	do
		echo "${pid}"
	done
	
	for (( k = 0; k < j; k++ ))
	do
		wait ${pid_pool[${k}]}
		if [ $? -ne 0 ]
		then
			echo "job failed, job_index = ${k}, pid = ${pid_pool[${k}]}"
			exit 1
		else
			echo "job complete, job_index = ${k}, pid = ${pid_pool[${k}]}"
		fi
	done
done
echo "All jobs finished!"
