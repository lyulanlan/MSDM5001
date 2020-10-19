time={1..100}
for i in time  
 do 
 mkdir "DDM${i}" 
 echo "nanoseconds since 1970-01-01 00:00:00 UTC:\n"$(date "+%s%N") > "DDM${i}/time_till_now.txt" 
 done 