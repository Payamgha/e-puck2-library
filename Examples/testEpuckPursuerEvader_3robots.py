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
    epk1 = epuck(port='COM12',debug=False) #4246
    epk2 = epuck(port='COM15',debug=False) #4313
    #epk3 = epuck(port='COM22',debug=False) #4312
    epk4 = epuck(port='COM29',debug=False) #4250
    
    robotList = (epk1,epk2,epk4)
    nRobot = len(robotList)
    while True:
        try:
            for i in range(nRobot):
                robot = robotList[i]
                N = robot.getProximitySensor()
                print(N)
                if i == 0:
                    if N[0] > 400 and N[7] > 400:
                        robot.setMotorSpeed(0,0)
                    else:
                        robot.setMotorSpeed(110,120)
                elif i == 1:
                    if N[0] < 100 and N[7] < 100:
                        robot.setMotorSpeed(150,150)
                    elif N[0] > 110 and N[7] > 110:
                        robot.setMotorSpeed(0,0)
                    elif N[7] - N[0] > 50:
                        robot.setMotorSpeed(0,200)
                    elif N[0] - N[7] > 50:
                        robot.setMotorSpeed(200,0)
                else:
                    if N[0] < 100 and N[7] < 100:
                        robot.setMotorSpeed(180,180)
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