cd /Users/baidu/Desktop/my-hadoop-streaming-jobs/click_q/script
if [ -f ../log/test_mapper.log ]
then
	rm ../log/test_mapper.log
fi

cp ../lib/utils.py .
cat ../resource/base_ue_example_1 | python mapper.get_click.py ../resource/20150922_cn_dict.txt > ../log/test_mapper.log

if [ $? == 0 ] && [ -f utils.py ]
then 
	rm utils.py
	rm utils.pyc
fi

cat ../log/test_mapper.log
