import os
import time

class Timer:
    def get_rounds(self):
        print('Input amount of rounds ')
        self.rounds = int(input())

    def get_time(self):
        print('Input seconds ')
        self.seconds = int(input())

    def get_recreation_time(self):
        print('Input recriation seconds ')
        self.recreation_seconds = int(input())

    def alarm(self):
        for i in range(0, self.rounds):
            time.sleep(self.seconds)
            file = "assets/alarm.wav"
            os.system("parole " + file)
            self.recreation()


    def recreation(self):
        os.system()
        print('get rest on {} seconds'.format(self.recreation_seconds))
        time.sleep(self.recreation_seconds)
