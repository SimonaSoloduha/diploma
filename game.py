# -*- coding: utf-8 -*-

# pip install -r requirements.txt

from kiseliova import SimonDrone, SimonScene

if __name__ == '__main__':
    scene = SimonScene(
        speed=10,
        asteroids_count=10,
    )
    drones = [SimonDrone() for _ in range(5)]
    scene.go()

# Первый этап: зачёт!
# Второй этап: зачёт!
