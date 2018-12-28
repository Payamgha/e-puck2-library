from epuck import epuck
import time 

epk1 = epuck(port='COM15',debug=False)
epk2 = epuck(port='COM22',debug=False)

while True:
    try:
        cmd = "Nope" #input("Enter command or 'exit':")
            # for Python 3
        if cmd == 'exit':
            epk1.setMotorSpeed(0,0)
            epk2.setMotorSpeed(0,0)
            epk1.close()
            epk2.close()
        else:
            N = epk1.getProximitySensor()
            print(N)
            if N[0] < 100 and N[7] < 100:
                epk1.setMotorSpeed(100,100)
            elif N[0] > 400 and N[7] > 400:
                epk1.setMotorSpeed(0,0)
            elif N[0] > 300:
                epk1.setMotorSpeed(100,0)
            elif N[7] > 300:
                epk1.setMotorSpeed(0,100)
            N = epk2.getProximitySensor()
            print(N)
            if N[0] < 100 and N[7] < 100:
                epk2.setMotorSpeed(300,300)
            elif N[0] > 300 and N[7] > 300:
                epk2.setMotorSpeed(0,0)
            elif N[7] - N[0] > 50:
                epk2.setMotorSpeed(0,100)
            elif N[0] - N[7] > 50:
                epk2.setMotorSpeed(100,0)
                
        time.sleep(0.005)
    except:
            epk1.setMotorSpeed(0,0)
            epk2.setMotorSpeed(0,0)
            epk1.close()
            epk2.close()
