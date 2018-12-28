import serial
  
port = "COM12"
baud = 115200
end = '\x0d\x0a'  
ser = serial.Serial(port, baud, timeout=1)
    # open the serial port

def getData(cmd):
    ser.write(cmd.encode()+end.encode())
    out = ser.readline()
    return out

def sendCmd(cmd):
    ser.write(cmd.encode()+end.encode())
    
def getAccelerometer():
    cmd = 'A'
    acc = [-1,-1,-1]
    out = getData(cmd)
    out = str(out, 'utf-8')
    print(out)
    isStart = False
    if out[0] == 'a':
        j = 0
        for i in range(len(out)):
            if isStart:
                if out[i] == ',':
                    acc[j] = int(data)
                    j = j + 1
                    isStart = False
                else:
                    data=data+out[i]
            if out[i] == ',':
                isStart = True
                data = ''
        acc[j] = int(data)
    return acc

def getMotorSpeed():
    cmd = 'E'
    vel = [-1,-1]
    out = getData(cmd)
    out = str(out, 'utf-8')
    print(out)
    if out[0] == 'e':
        isStart = False
        j = 0
        for i in range(len(out)):
            if isStart:
                if out[i] == ',':
                    vel[j] = int(data)
                    j = j + 1
                    isStart = False
                else:
                    data=data+out[i]
            if out[i] == ',':
                isStart = True
                data = ''
        vel[j] = int(data)
    return vel

def setMotorSpeed(velRight=500,velLeft=500):
    cmd = 'E'
    out = sendCmd(cmd)

def getProximitySensor():
    cmd = 'N'
    proximitySensor = [-1,-1,-1,-1,-1,-1,-1,-1]
    out = getData(cmd)
    out = str(out, 'utf-8')
    print(out)
    if out[0] == 'n':
        isStart = False
        j = 0
        for i in range(len(out)):
            if isStart:
                if out[i] == ',':
                    proximitySensor[j] = int(data)
                    j = j + 1
                    isStart = False
                else:
                    data=data+out[i]
            if out[i] == ',':
                isStart = True
                data = ''
        proximitySensor[j] = int(data)
    return proximitySensor

def getAmbientLightSensor():
    cmd = 'O'
    ambientLightSensor = [-1,-1,-1,-1,-1,-1,-1,-1]
    out = getData(cmd)
    out = str(out, 'utf-8')
    print(out)
    if out[0] == 'n':
        isStart = False
        j = 0
        for i in range(len(out)):
            if isStart:
                if out[i] == ',':
                    ambientLightSensor[j] = int(data)
                    j = j + 1
                    isStart = False
                else:
                    data=data+out[i]
            if out[i] == ',':
                isStart = True
                data = ''
        ambientLightSensor[j] = int(data)
    return ambientLightSensor

if ser.isOpen():
     print(ser.name + ' is open...')

while True:
    cmd = input("Enter command or 'exit':")
        # for Python 3
    if cmd == 'exit':
        ser.close()
        exit()
    else:
        out = getAccelerometer()
        print('Receiving: '+str(out))
        out = getMotorSpeed()
        print('Receiving: '+str(out))
        