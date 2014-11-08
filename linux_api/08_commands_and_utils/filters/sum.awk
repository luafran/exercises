{ sum[$1] += $2 }
END { for (name in sum) print name, sum[name] }
