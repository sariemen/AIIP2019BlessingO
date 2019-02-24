# Program to generate a data set with  floats to fix a sensor problem
import random as rand
import datetime as dt
import sys

sensorData = []

# Function to import random floats into a list
def sensorAndErrorExcept():
    try:
        for i in range(16):
            sensorDataValue = rand.random()
            sensorData.append(sensorDataValue)
            return (sensorData)
            break
    except ValueError:
        print("error")
        raise

#Use list comprehension to create a list with the 32 sensors

Cluster = [sensorAndErrorExcept() for i in range(32)]

SensorCluster = list(enumerate(Cluster,1))

with open ('Sensor Data.txt', 'a') as f:
    f.write(dt.datetime.now().ctime())
    f.write("%s\n" %SensorCluster)



# Function to check string errors

def ErrorException():
    try:
        with open('Sensor Data.txt') as sf:
            l = sf.readline()
            fl = float(sensorData)
    except ValueError:
        print('error')










