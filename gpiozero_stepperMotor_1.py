# -*- condig: uft-8 -*-

from gpiozero import DigitalOutputDevice
from time import sleep

class StepperBi4():
    def __init__(self, A=None, Am=None, B=None, Bm=None):
        self.phase = 0
        self.gpios=tupel(DigitalOutputDevice(pin) for pin in (A, B, Am, Bm) )
        self.halfstepSeq = [
                            [1,0,0,0],
                            [1,1,0,0],
                            [0,1,0,0],
                            [0,1,1,0],
                            [0,0,1,0],
                            [0,0,1,1],
                            [0,0,0,1],
                            [1,0,0,1]
                            ]
        def setPhase(self,phase):
            self.phase=phase
            for gpio, state in zip(self.gpios, self.halfstepSeq[phase]):
                gpio.value=state
                
        def stepForward(self):
            self.phase = (self.phase + 1) % 8
            self.sefPhase(self.phase)

        def stepReverse(self):
            self.phase = (self.phase - 1) % 8
            self.sefPhase(self.phase)


step = StepperBi4(4, 17, 27, 22)
step.setPhase(0)

try:
    while True:
        sleep(1)
        step.stepForward()
        sleep(1)
        step.stepReverse
        sleep(1)        


except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
except KeyboardInterrupt:
    print("키보드 중단")
finally:
    print("프로그램이 종료되었습니다.)                        
