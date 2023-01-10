import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for loop in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(loop)

p.disconnect()