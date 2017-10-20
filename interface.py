from threading import Thread
import signal
import sys

class Interface(Thread):
   
   def __init__(self):
      return None
   
   def run(self):
      



   def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()
