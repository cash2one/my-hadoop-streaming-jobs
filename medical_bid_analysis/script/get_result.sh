source ../conf/conf.sh $1
timestamp=`date +%Y%m%d-%H_%M_%S`

for (( i = 0 ; i <= 9 ; i ++ ))
do
	
	result=`${HADOOP} fs -cat "${meta_result_path}${shitu_type}/meta-e${experimental_list[${i}]}-c${control_list[${i}]}/part-00000"` 
	echo ${result}
	echo ${result} | awk '{if ($1 == 0) print $2, $3, $4}' >> ../resource/meta_res.non_medical.${timestamp}.data
	echo ${result} | awk '{if ($5 == 1) print $6, $7, $8}' >> ../resource/meta_res.medical.${timestamp}.data
done
