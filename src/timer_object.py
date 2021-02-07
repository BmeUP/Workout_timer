import os
import time
import subprocess

class Timer:
    def check_sox(self):
        try:
            subprocess.call('sox')
            subprocess.call('clear')
        except FileNotFoundError:
            print('You should install sox')
            print('You can do it by command -- apt install sox')
            import sys
            sys.exit()

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
            duration = 2  # seconds
            freq = 440  # Hz
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
            self.recreation()


    def recreation(self):
        print('get rest on {} seconds'.format(self.recreation_seconds))
        time.sleep(self.recreation_seconds)

timer = Timer()
