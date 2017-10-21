from threading import Thread
from math import cos
from math import sin
#import RPi.GPIO as GPIO

#On définit le zero degree VERS LE BAS dans MA carte

class Ultrason(Thread):
   
   def __init__(self,robot,carte,echo_pin, trigger_pin):
      
      self.carte = carte
      self.robot = robot
      self.echo_pin = echo_pin 
      self.trigger_pin = trigger_pin
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(echo_pin,GPIO.IN)
      GPIO.setup(trigger_pin,GPIO.OUT)
      return
      
      
   
   def run(self):
      return None
      
   def verification(self,distance):
      """Cette fonction a pour objectif de voir si l'obstacle détecté est déjà présent sur la carte"""
      donnees = robot.get_donnees()
      theta = donnees[2]/360 * 2*3.14
      x = donnees[0]
      y = donnees[1]
      x_obstacle = int((x+distance*cos(theta))/dx)
      y_obstacle = int((y-distance*sin(theta))/dx)
      self.carte.verification(x_obstacle,y_obstacle)
      
      return None
      
      
   
   
   
   
   
   
