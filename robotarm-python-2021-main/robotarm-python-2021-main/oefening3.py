from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5

for x in range(1,5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
