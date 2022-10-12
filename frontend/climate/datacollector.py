import serial
import mysql.connector
import time
from datetime import datetime

def collect(times):
    localConfig = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'senseDB'
    }

    cn = mysql.connector.connect(**localConfig)
    cr = cn.cursor()

    port = 'COM3'
    print("Trying...", port)
    test = serial.Serial(port=port, baudrate=9600, timeout=10)

    temp = test.readline().decode('utf-8')
    humidity = test.readline().decode('utf-8')
    while temp is not None and '-999' not in temp:
        for i in range(0, times+1):
            temp = float(temp.split('=')[1][0:6])
            humidity = int(humidity.split('=')[1][0:3])
            date = str(datetime.now()).split(' ')
            date = date[1][0:8]
            print(temp, humidity, date)
            cr.execute(f"INSERT INTO data (collectorID, temp, humidity, date) VALUES (1, {temp}, {humidity}, '{date}')")
            cr.execute("SELECT * FROM data")
            res = cr.fetchall()
            print(res[-1])
            cn.commit()
            time.sleep(2)
            temp = test.readline().decode('utf-8')
            humidity = test.readline().decode('utf-8')
        cn.close()
        exit()
    cn.close()

if __name__ == '__main__':
    collect(10)

