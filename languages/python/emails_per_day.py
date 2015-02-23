data1 = [
    {'name': 'Sue', 'date': '2014-01-01', 'nr_emails': 10},
    {'name': 'Sue', 'date': '2014-01-02', 'nr_emails': 3},
    {'name': 'Bob', 'date': '2014-01-01', 'nr_emails': 20},
    {'name': 'Bob', 'date': '2014-01-02', 'nr_emails': 1},
]

data2 = [
    {'name': 'Sue', 'date': '2014-01-01', 'hours_worked': 4},
    {'name': 'Sue', 'date': '2014-01-02', 'hours_worked': 4},
    {'name': 'Bob', 'date': '2014-01-01', 'hours_worked': 8},
    {'name': 'Bob', 'date': '2014-01-02', 'hours_worked': 8},
    {'name': 'Peter', 'date': '2014-01-01', 'hours_worked': 8},
]

#var data3 = [
#    { name: 'Sue', date: '2014-01-01', emails_per_hour: 2.5 },
#    { name: 'Sue', date: '2014-01-02', emails_per_hour: x.x },
#    ...
#];

data3 = []
for d2 in data2:
    name = d2.get('name')
    date = d2.get('date')
    hours = int(d2.get('hours_worked'))

    #print 'name:', name, 'date:', date

    nr_emails = 0
    for d1 in data1:
        if d1.get('name') == name and d1.get('date') == date:
            nr_emails = int(d1.get('nr_emails'))
            break

    emails_per_hour = nr_emails / float(hours)
    result = {
        'name': name,
        'date': date,
        'emails_per_hour': emails_per_hour
    }

    #print result

    data3.append(result)

print data3