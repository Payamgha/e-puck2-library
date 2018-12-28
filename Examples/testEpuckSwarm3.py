from epuck import epuck
import time 
import math

OBSTACL_THRESHOLD = 400

def setVelocity(robot,vel,N):
    if N[0] > OBSTACL_THRESHOLD and N[7] > OBSTACL_THRESHOLD:
        robot.setMotorSpeed(0,0)
    else:
        robot.setMotorSpeed(vel[0],vel[1])

def getAlignment(vel):
    n = len(vel[:,0])
    v = [sum(vel[:,0])/n, sum(vel[:,1])/n]
    return v
    
def shutdown(robotList):
    nRobot = len(robotList)
    for i in range(nRobot):
        robot = robotList[i]
        robot.setMotorSpeed(0,0)
    for i in range(nRobot):
        robot = robotList[i]
        robot.close()
        
def main():
    epk1 = epuck(port='COM15',debug=False) #4313
    epk2 = epuck(port='COM22',debug=False) #4312
    epk3 = epuck(port='COM12',debug=False) #4246
    
    odom = [[0,0,0],
            [0,0.1,0],
            [0,0.2,0]]
    vel = [[0,0],
            [0,0],
            [0,0]]
    robotList = (epk1,epk2,epk3)
    nRobot = len(robotList)
    while True:
        try:
            for i in range(nRobot):
                robot = robotList[i]
                N = robot.getProximitySensor()
                odom[i,:] = robot.getOdometry()
                print(N)
                setVelocity(robot,vel[i,:],N)        
        except KeyboardInterrupt:
            shutdown(robotList)
        except EOFError:
            print(EOFError)
            shutdown(robotList)
        except:
            shutdown(robotList)
        time.sleep(0.001)
        

if __name__ == "__main__":
    main()