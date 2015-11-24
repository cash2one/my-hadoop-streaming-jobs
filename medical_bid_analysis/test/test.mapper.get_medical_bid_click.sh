cp ../script/*.py .
cp ../lib/*.so .
cat ../resource/bad_case.base_ue_wise_sample | python mapper.get_medical_bid_click.py wise | sort -k 1,1 -k 2,2 -k 3,3 | python reducer.sum_average_bid_click.py 2> error.log > output.log
rm *.py *.so
