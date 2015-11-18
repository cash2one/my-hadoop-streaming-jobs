cp ../lib/* .
cat ../resource/online_wise_evaluation.txt ../resource/word_url_relq | python mapper.set_tag.py | sort -k 1,1 -k 2,2 -k 3,3 | python reducer.merge.py > ../log/merge_output
rm url_util.*