from question import Question
import random
class Chord_Question(Question):

  #possible_inputs = ['C', 'B#', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'Fb', 'F', 'E#', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', "Cb", " "] #why is the space there
  possible_inputs = ['C', 'B#', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'Fb', 'F', 'E#', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', "Cb"]
  chord_options = ["M", "m", "aug", "dim"]

  def __call__(self):
    chord_name = random.choice(Chord_Question.chord_options)
    show, answer = self.create(chord_name)
    print(show)
    user_guess = self.inp()
    Question.check_user_input_enharmonic(user_guess, answer)

  def create(self, whatta):
    #start_note is the key, first_loc is the location of the first note in the key on the keyboard, n is the number of accidentals,
    start_note, first_loc, n = Question.numOnCircle() 

    #start, j, n = numOnCircle()

    #find what to add
    #x is the first distance
    #xx is the second distance
    if whatta == "M":
      x = 4
      xx = 3
    elif whatta == "m":
      x = 3
      xx = 4
    elif whatta == "aug":
      x = 4
      xx = 4
    else:
      x = 3
      xx = 3

    two = (x + first_loc) % 12
    three = (xx + two) % 12

    middle_note = Question.on_keyboard[two]
    end_note = Question.on_keyboard[three]

    q = random.randint(0,1)
    if type(middle_note) is list:
      middle_note = middle_note[q]
    q = random.randint(0,1)
    if type(end_note) is list:
      end_note = end_note[q]

    show = f"What is the {whatta} chord of {start_note}"
    answer = start_note + "-" + middle_note + "-" + end_note
    return show, answer

  def inp(self):
    guess = input("Answer: ").strip()
    while (Chord_Question.bad_input(guess.split("-"))):
      print("case sensitive, beware the letters you type")
      guess = input("Answer: ").strip()
    return guess

  def bad_input(guess):
    for i in guess:
      if i not in Chord_Question.possible_inputs:
        return True
    else:
      return False
