#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def cleanup(port):
    print("cleanup " + str(port))
    
def output(port, state):
    print("set " + str(port) + " to " + str(state))

def setup(port, state):
    print("setup " + str(port) + " to " + str(state))

def setmode(mode):
    print("set mode to " + mode)

OUT = "OUT"
IN = "IN"
BOARD = "BOARD"
BCM = "BCM"