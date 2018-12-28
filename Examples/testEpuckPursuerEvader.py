from epuck import epuck
import time 

def main():
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
                if N[0] > 400 and N[7] > 400:
                    epk1.setMotorSpeed(0,0)
                else:
                    epk1.setMotorSpeed(250,300)#(100,150)
                N = epk2.getProximitySensor()
                print(N)
                if N[0] < 150 and N[7] < 150:
                    epk2.setMotorSpeed(350,350)#(200,200)
                elif N[0] > 300 and N[7] > 300:
                    epk2.setMotorSpeed(0,0)
                elif N[7] - N[0] > 50:
                    epk2.setMotorSpeed(0,400)
                elif N[0] - N[7] > 50:
                    epk2.setMotorSpeed(400,0)
                    
            time.sleep(0.005)
        except:
                epk1.setMotorSpeed(0,0)
                epk2.setMotorSpeed(0,0)
                epk1.close()
                epk2.close()

if __name__ == "__main__":
    main()