from epuck import epuck
import time 

def main():
    epk1 = epuck(port='COM15',debug=False)
    #epk2 = epuck(port='COM22',debug=False)

    while True:
        try:
            cmd = "Nope" #input("Enter command or 'exit':")
            if cmd == 'exit':
                epk1.setMotorSpeed(0,0)
                epk1.close()
                #epk2.close()
            else:
                epk1.setMotorSpeed(500,500)
                odom1 = epk1.getOdometry()
                #odom2 = epk2.getOdometry()
                print(odom1)
                #print(odom2)
            time.sleep(0.01)
        except:
                epk1.setMotorSpeed(0,0)
                epk1.close()
                #epk2.close()

if __name__ == "__main__":
    main()