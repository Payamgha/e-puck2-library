from epuck import epuck
import time 

def shutdown(robotList):
    nRobot = len(robotList)
    for i in range(nRobot):
        robot = robotList[i]
        robot.setMotorSpeed(0,0)
    for i in range(nRobot):
        robot = robotList[i]
        robot.close()
        
def main():
    #epk1 = epuck(port='COM12',debug=False) #4246
    epk2 = epuck(port='COM15',debug=False) #4313
    epk3 = epuck(port='COM22',debug=False) #4312
    
    robotList = (epk2,epk3)
    nRobot = len(robotList)
    while True:
        try:
            for i in range(nRobot):
                robot = robotList[i]
                N = robot.getProximitySensor()
                print(N)
                if N[0] < 100 and N[7] < 100:
                    robot.setMotorSpeed(150,150)
                elif N[0] > 110 and N[7] > 110:
                    robot.setMotorSpeed(0,0)
                elif N[7] - N[0] > 50:
                    robot.setMotorSpeed(0,200)
                elif N[0] - N[7] > 50:
                    robot.setMotorSpeed(200,0)
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