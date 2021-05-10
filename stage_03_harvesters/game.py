# -*- coding: utf-8 -*-

from stage_03_harvesters.driller import DrillerDrone
from kiseliova import SimonDrone, SimonScene

NUMBER_OF_DRONES = 5

if __name__ == '__main__':
    scene = SimonScene(
        speed=5,
        asteroids_count=20,
    )
    team_1 = [SimonDrone() for _ in range(NUMBER_OF_DRONES)]
    team_2 = [DrillerDrone() for _ in range(NUMBER_OF_DRONES)]
    scene.go()

# 9/10 побед!
# зачёт!
