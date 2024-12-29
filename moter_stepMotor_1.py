# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:28:54 2022

@author: hanuri
"""

from gpiozero import DigitalOutputDevice
from time import sleep

class StepperBi4():
    def __init__(self, A=None, Am=None, B=None, Bm=None):
        self.phase = 0
        self.gpios = tuple(DigitalOutputDevice(pin) for pin in (A, B, Am, Bm))
        self.halfstepSeq = [
                            [1,0,0,0],
                            [1,1,0,0],
                            [0,1,0,0],
                            [0,1,1,0],
                            [0,0,1,0],
                            [0,0,1,1],
                            [0,0,0,1],
                            [1,0,0,0]
            ]
        
    def setPhase(self, phase):
        self.phase = phase
        for gpio, state in zip(self.gpios, self.halfstepSeq[phase]):
            gpio.value = state
                
    def stepForward(self):
        self.phase = (self.phase + 1) % 8
        self.setPhase(self.phase)
        
    def stepReverse(self):
        self.phase = (self.phase - 1) % 8
        self.setPhase(self.phase)

step = StepperBi4(6, 13, 19, 26)
step.setPhase(0)

while True:
    sleep(0.01)
    step.stepForward()

