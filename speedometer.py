# Author: Ananta Jamdhade
# Date  : 30/06/2019
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation.

# Discription : Data will tack from serialy and show it on Spedometer GUI
 
from tkinter import *
import tkinter as tk
import datetime
import tk_tools
import serial

root = tk.Tk()

gauge = tk_tools.Gauge(root, width=500, height=300, min_value=0.0, max_value=200.0, label='speed', divisions=10, yellow=50, red=80, yellow_low=0, red_low=0,
bg='white')
gauge.grid()
value = 0;



def init_serial():
    global ser          
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = "COM0"   #COM Port Name Start from 0
    #Specify the TimeOut in seconds, so that SerialPort
    #Doesn't hangs
    ser.timeout = 10
    ser.open()          #Opens SerialPort
    # print port open or closed
    if ser.isOpen():
        print("Open: " + ser.portstr)
        
init_serial()
def clock():
    global value
    bytes = ser.readline()  #Read from Serial Port
    #print ("You sent: ")      
    value = int(bytes)
    #print (bytes)          #Print What is Read from Port
    gauge.set_value(value)
    root.after(10, clock) # run itself again after 10 ms

clock()

root.mainloop()

