
battle_field0 = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

battle_field1 = [
    ['X', 'X', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

battle_field2 = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', 'X', 'X', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

battle_field3 = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', 'X', 'X'],
]

battle_field4 = [
    ['X', '.', '.', '.', '.', '.'],
    ['X', '.', '.', '.', '.', '.'],
    ['X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

battle_field5 = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

battle_field6 = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', 'X'],
]

def bomb_location(x, y):
    if battle_field[y][x] == 'X':
        return True
    else:
        return False


def find_battleship(grid_size):
    # print 'grid_size:', grid_size
    ship = False
    for y in range(0, grid_size):
        for x in range(0, grid_size):
            if bomb_location(x, y):
                ship = True
                if x+1 < grid_size and bomb_location(x+1, y):
                    return (x, y), (x+1, y), (x+2, y)
                else:
                    return (x, y), (x, y+1), (x, y+2)
    if not ship:
        return None

def print_battlefield(battle_field):
    grid_size = len(battle_field[0])
    for y in range(0, grid_size):
        print battle_field[y]

def test_battlefield(battle_field):
    grid_size = len(battle_field[0])
    print 'grid_size =', grid_size
    for y in range(0, grid_size):
        for x in range(0, grid_size):
            print '[x={0},y={1}] {2}'.format(x, y, bomb_location(x, y))

print 'battle_field0'
battle_field=battle_field0
print_battlefield(battle_field)
location  = find_battleship(len(battle_field[0]))
print 'ship is in:', location

print 'battle_field1'
battle_field=battle_field1
print_battlefield(battle_field)
location  = find_battleship(len(battle_field[0]))
print 'ship is in:', location

print 'battle_field2'
battle_field=battle_field2
print_battlefield(battle_field)
location  = find_battleship(len(battle_field[0]))
print 'ship is in:', location

print 'battle_field3'
battle_field=battle_field3
print_battlefield(battle_field)
location  = find_battleship(len(battle_field[0]))
print 'ship is in:', location

print 'battle_field4'
battle_field=battle_field4
print_battlefield(battle_field)
location  = find_battleship(len(battle_field[0]))
print 'ship is in:', location

print 'battle_field5'
battle_field=battle_field5
print_battlefield(battle_field)
location  = find_battleship(len(battle_field[0]))
print 'ship is in:', location

print 'battle_field6'
battle_field=battle_field6
print_battlefield(battle_field)
location  = find_battleship(len(battle_field[0]))
print 'ship is in:', location

