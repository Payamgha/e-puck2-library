from epuck import epuck
import time 

def main():
    epk1 = epuck(port='COM15',debug=False)
    #epk2 = epuck(port='COM22',debug=False)

    while True:
        try:
            cmd = "Nope" #input("Enter command or 'exit':")
                # for Python 3
            if cmd == 'exit':
                epk1.setMotorSpeed(0,0)
                epk1.close()
                #epk2.close()
            else:
                epk1.setMotorSpeed(0,0)
                N = epk1.getProximitySensor()
                print(N)
            time.sleep(1)
        except:
                epk1.setMotorSpeed(0,0)
                epk1.close()
                #epk2.close()

if __name__ == "__main__":
    main()