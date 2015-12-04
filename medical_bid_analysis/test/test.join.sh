cp ../script/*.py .
cp ../lib/*.so .
cp ../lib/*.py .
timestamp=`date +%Y:%m:%d-%H:%M:%S`
cat ../resource/bidword.intersection.wise.10 ../resource/bidword_domain.wise.02 | python mapper.count_filter.py 5 02 01 | sort -k 1,1 -k 2,2 -k 3,3 | python reducer.join_bidword_domain.py 2> log/join.${timestamp}.error.log > log/join.${timestamp}.output.log
rm *.py *.so *.pyc
