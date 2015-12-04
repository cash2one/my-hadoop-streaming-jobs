cp ../script/*.py .
cp ../lib/*.so .
cp ../lib/*.py .
timestamp=`date +%Y:%m:%d-%H:%M:%S`
cat ../resource/base_ue_pc_11_part_00399 | python mapper.get_medical_bid_click.py pc #| sort -k 1,1 -k 2,2 -k 3,3  | python reducer.sum_average_bid_click.py 03 2> log/get_bidword_domain.${timestamp}.error.log > log/get_bidword_domain.${timestamp}.output.log
rm *.py *.so *.pyc
