from epuck import epuck

def main():
    epk = epuck(port='COM15')

    while True:
        cmd = input("Enter command or 'exit':")
            # for Python 3
        if cmd == 'exit':
            epk.close()
        else:
            out = epk.getAccelerometer()
            print('Receiving: '+str(out))
            out = epk.getMotorSpeed()
            print('Receiving: '+str(out))

if __name__ == "__main__":
    main()