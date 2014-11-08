cat $* |
tr -sc A-Za-z '\n' |
sort |
uniq -c |
sort -n |
tail -5 
