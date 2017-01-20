d1 = [
    {'name': 'Sue', 'date': '2014-01-01', 'nr_emails': 10},
    {'name': 'Sue', 'date': '2014-01-02', 'nr_emails': 3},
    {'name': 'Bob', 'date': '2014-01-01', 'nr_emails': 20},
    {'name': 'Bob', 'date': '2014-01-02', 'nr_emails': 1},
]

d2 = [
    {'name': 'Sue', 'date': '2014-01-01', 'hours_worked': 4},
    {'name': 'Sue', 'date': '2014-01-02', 'hours_worked': 4},
    {'name': 'Bob', 'date': '2014-01-01', 'hours_worked': 8},
    {'name': 'Bob', 'date': '2014-01-02', 'hours_worked': 8},
    {'name': 'Peter', 'date': '2014-01-01', 'hours_worked': 8},
]


# var data3 = [
#    { name: 'Sue', date: '2014-01-01', emails_per_hour: 2.5 },
#    { name: 'Sue', date: '2014-01-02', emails_per_hour: x.x },
#    ...
# ];


def emails_per_day2(data1, data2):
    data3 = []

    for r in zip(data1, data2):
        # print r
        name = r[0].get('name')
        date = r[0].get('date')
        nr_emails = r[0].get('nr_emails')
        hours = int(r[1].get('hours_worked'))
        emails_per_hour = nr_emails / float(hours)

        res = {
            'name': name,
            'date': date,
            'emails_per_hour': emails_per_hour
        }

        data3.append(res)

    return data3


if __name__ == '__main__':
    result = emails_per_day2(d1, d2)
    for rec in result:
        print rec
