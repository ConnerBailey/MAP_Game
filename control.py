import time
from map2 import Map

map_ = Map(16, 20)


def iter():
    step()
    map_.print_map()
    print()


def step():
    map_.move_up()

map_.print_map()
print()
time.sleep(1)

while True:
    iter()
    time.sleep(1)
    
