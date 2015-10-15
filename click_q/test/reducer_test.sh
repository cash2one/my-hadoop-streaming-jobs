cd /Users/baidu/Desktop/my-hadoop-streaming-jobs/click_q/script
if [ -f ../log/test_reducer.log ]
then
	rm ../log/test_reducer.log
fi

cat ../resource/reducer_test_sample.txt | python reducer.click_q.py > ../log/test_reducer.log