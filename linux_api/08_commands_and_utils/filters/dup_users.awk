BEGIN { FS = ":" }

{
    user = $1
    uid = $3
    count[uid] += 1;

    if (count[uid] < 2)
        users[uid] = users[uid] user
    else
        users[uid] = users[uid] "," user
    #print uid, users[uid]
}

END {
    for (uid in users)
        if (split(users[uid], u, ",") > 1)
            print "uid", uid, "has duplicated users:", users[uid]
}
