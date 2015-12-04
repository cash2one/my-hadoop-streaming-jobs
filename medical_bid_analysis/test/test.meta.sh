cp ../script/*.py .
cp ../lib/*.so .
cp ../lib/*.py .
timestamp=`date +%Y:%m:%d-%H:%M:%S`
cat ../resource/bidword.intersection.wise.10-11.00019 | python mapper.split_field.py 10 11 | sort -k 1,1 -k 2,2 -k 3,3 #| python reducer.compute_theta_error.py 2> log/meta.${timestamp}.error.log > log/meta.${timestamp}.output.log
rm *.py *.so *.pyc
