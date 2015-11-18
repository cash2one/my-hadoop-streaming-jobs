cat ../log/new_merge_output | python mapper.set_tag_for_q.py > ../log/split_q_tmp
cat ../log/split_q_tmp | python reducer.output_q.py rigq > ../log/auc_rigq_mark3
cat ../log/split_q_tmp | python reducer.output_q.py qlq > ../log/auc_qlq_mark3
cat ../log/split_q_tmp | python reducer.output_q.py clickq > ../log/auc_clickq_mark3
rm ../log/split_q_tmp