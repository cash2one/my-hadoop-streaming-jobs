cat ../resource/wise.222_223.20151222.a0000.00099 | python ../script/mapper.get_count.py > ../resource/tmp.part1
cat ../resource/wise.222_223.20151222.a0000.00099 | python ../script/mapper.get_count.py > ../resource/tmp.part2

cat ../resource/tmp.part1 ../resource/tmp.part2 | sort -k 1,1 | python ../script/reducer.merge_count.py > result
