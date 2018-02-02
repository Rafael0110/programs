rm countAttack.txt
touch countAttack.txt
echo 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 >> countAttack.txt
echo 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 >> countAttack.txt
ls | grep log | awk '{print "python", "calc_attack_count.py", $1 }' | sh