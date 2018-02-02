rm countVictory.txt
touch countVictory.txt
echo 0,0,0,0 >> countVictory.txt
echo 0,0,0,0 >> countVictory.txt
echo 0,0,0,0 >> countVictory.txt
ls | grep log | awk '{print "python", "calc_victory_count.py", $1 }' | sh