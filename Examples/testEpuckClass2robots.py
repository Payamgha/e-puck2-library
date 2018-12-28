from epuck import epuck

def main():
    epk1 = epuck(port='COM15')
    epk2 = epuck(port='COM22')

    while True:
        cmd = input("Enter command or 'exit':")
            # for Python 3
        if cmd == 'exit':
            epk1.setMotorSpeed(0,0)
            epk1.close()
            epk2.close()
        else:
            #out = epk1.getAccelerometer()
            #print('Receiving 1: '+str(out))
            #out = epk2.getAccelerometer()
            #print('Receiving 2: '+str(out))
            #out = epk1.getMotorSpeed()
            #print('Receiving 1: '+str(out))
            #out = epk2.getMotorSpeed()
            #print('Receiving 2: '+str(out))
            epk1.setMotorSpeed(100,100)
            odom1 = epk1.getOdometry()
            odom2 = epk2.getOdometry()
            print(odom1);
            print(odom2);
            
if __name__ == "__main__":
    main()