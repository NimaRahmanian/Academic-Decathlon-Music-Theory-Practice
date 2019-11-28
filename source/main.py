from interval import Interval_Question
from scale import Scale_Question
from chord import Chord_Question
import random

tutorial_message = """Intervals are typed as follows:
Majors with capital M and Minor with lower m.\nExample: m7.\nChords and Scales are typed with notes separated by dashes.\nExample: A-B-C.\nFor chords and scales, be sure to type Capital letters only!\n""" 
print(tutorial_message)


interval = Interval_Question()
scale = Scale_Question()
chord = Chord_Question()
while True:
  interval()
  scale()
  chord()


"""
score = 0
while (score < 6):
  #random problem, add to score if correct
  x = random.randint(0, 2)
  if x == 0:
    correct = scale()
  elif x == 1: 
    correct = interval()
  else:
    correct = chord()

  if correct:
    score += 1
"""
