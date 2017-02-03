

class HashTable:
    def __init__(self):
        self.size = 5
        self.slots = [list() for _ in range(self.size)]
        #self.data = [list] * self.size

    def put(self, key, value):
        hash_value = self.hash_function(key, len(self.slots))
        item = {
            'key': key,
            'value': value
        }
        self.slots[hash_value].append(item)

    def get(self, key):
        hash_value = self.hash_function(key, len(self.slots))
        for item in self.slots[hash_value]:
            if item.get('key') == key:
                return item.get('value')
        return None

    def hash_function(self, key, size):
        return key % size


if __name__ == '__main__':
    table = HashTable()
    table.put(10, '10')
    table.put(27, '27')
    table.put(38, '38')
    table.put(4, '4')
    table.put(20, '10')

    print 'table len =', len(table.slots)
    for i in range(table.size):
        print 'table[{0}] has {1} elements'.format(i, len(table.slots[i]))
    value = table.get(10)
    print 'get(10) =', value
    value = table.get(99)
    print 'get(99) =', value