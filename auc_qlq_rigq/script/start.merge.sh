cp ../lib/* .
cat ../resource/merge_output ../resource/case_20151103_wise_ori_with_index | python mapper.set_tag.py | sort -k 1,1 -k 2,2 | python reducer.merge.py > ../log/new_merge_output
rm url_util.*