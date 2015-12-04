cur_dir=`pwd`
program="start.join.sh"
shitu_type=$1
#experimental_list=("01" "02" "03" "04" "05" "06" "07" "08" "09" "10")
#control_list=("02" "03" "04" "05" "06" "07" "08" "09" "10" "11")
batch_size=3

source ../conf/conf.sh ${shitu_type}

if [ ${#experimental_list[@]} != ${#control_list[@]} ]
then
	exit 1
fi

flag="0"
task_num=${#experimental_list[@]}
today_date=`date +%Y%m%d`

mkdir ../log/join.${today_date}
mkdir ../log/join.${today_date}/${shitu_type}

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

		echo "Starting Task ${j}, exp = ${experimental_list[${i}]}, con = ${control_list[${i}]}, shitu = ${shitu_type} ..."
		sh ${program} ${shitu_type} ${experimental_list[${i}]} ${control_list[${i}]} > ../log/join.${today_date}/${shitu_type}/task.${shitu_type}.${experimental_list[$[i]]}-${control_list[${i}]}.log 2>&1 &
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
