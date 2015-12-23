#!/bin/bash
#source ../conf/conf.sh
source ../lib/util.sh

if [ ! -d "../output/${owner_tag}.${task_tag}" ]
then
	echo_info "Creating new output path."
	mkdir ../output/${owner_tag}.${task_tag}
else
	echo_warning "The output path is existed. Removing the last result."
	rm ../output/${owner_tag}.${task_tag}/*
fi

cd ../output/${owner_tag}.${task_tag}

# Get data from hadoop
${HADOOP} fs -get "${output_base_path}/${dates}/part-00000" result.txt 

cd ..

echo_info "All results have been retrived. Please check /output"
