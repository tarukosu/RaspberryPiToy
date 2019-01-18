#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading

# import RPi.GPIO as GPIO
import GPIOMock as GPIO
GPIO.setmode(GPIO.BCM)

segment_ports = [14,4,23,8,7,10,18,25]
cathode_ports = [12,16]
# Number light pattern
character_pattern = {
    ' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}

class SevenSegmentDisplay:
    def __init__(self, common_port, segment_ports):
        self.common_port = common_port
        self.segment_ports = segment_ports
        GPIO.setup(common_port, GPIO.OUT)
        for p in self.segment_ports:
	        print(p)
            GPIO.setup(p, GPIO.OUT)
        self.hideCharacter()

    def __del__(self):
        print("destractor")
        self.hideCharacter()
        GPIO.cleanup(self.common_port)
        for p in self.segment_ports:
            GPIO.cleanup(p)

    def showCharacter(self, char):
        if char not in character_pattern:
            self.hideCharacter()
            return

        GPIO.output(self.common_port, False)

        pattern = character_pattern[char]
        for s, p in zip(pattern, self.segment_ports):
            GPIO.output(p, s == 0)

    def hideCharacter(self):
        GPIO.output(self.common_port, True)
        for p in self.segment_ports:
            GPIO.output(p, False)


class NumberDisplay(threading.Thread):
    def __init__(self):
        super(NumberDisplay, self).__init__()
        self.lock = threading.Lock()
        self.daemon = True
        self.interval = 0.1
        self.characters = ""
        self.seven_segments = []
        for p in cathode_ports:
            print(p)        
            seven_segment = SevenSegmentDisplay(p, segment_ports)
            self.seven_segments.append(seven_segment)

        #self.run()
        self.start()

    def run(self):
        while True:
            #print("run")
            with self.lock:
                characters = self.characters
                
            #print(characters)
            for segment, char in zip(self.seven_segments, characters[::-1]):
                # print(segment)
                # print(char)
                segment.showCharacter(str(char))
                time.sleep(self.interval)
                segment.hideCharacter()
            # time.sleep(self.interval)


    def set_num(self, num):
        with self.lock:
            self.characters = str(num)


if __name__ == "__main__":
    nd = NumberDisplay()
    # nd.start()

    time.sleep(1)
    nd.set_num(3)
    time.sleep(1)
    nd.set_num(1234)
    time.sleep(1)

    for i in range(100):
        nd.set_num(i)
        time.sleep(1)
