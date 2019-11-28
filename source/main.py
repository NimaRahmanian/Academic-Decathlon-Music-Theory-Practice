import random
class Question:
  #class variables
  circ = {0: "C" , 1: "G", 2: "D", 3: "A", 4: "E", 5: "B",
          6: "F#", 7: "C#", -1: "F", -2: "Bb", -3: "Eb",
        -4: "Ab", -5: "Db", -6: "Gb", -7: "Cb"}

  on_keyboard = {0: ["C", "B#"], 1: ["C#", "Db"], 2: "D", 3: ["D#", "Eb"], 4: ["E", "Fb"],
                5: ["F", "Eb"], 6: ["F#", "Gb"], 7: "G", 8: ["G#", "Ab"], 9: "A",
                10: ["A#", "Bb"], 11: ["B", "Cb"]}

  intervals = ["m2", "M2", "m3", "M3", "P4", "aug4, d5, TT", "P5", "m6", "M6", "m7", "M7", "P8"]

  key_lett = ["A", "B", "C", "D", "E", "F", "G"]
  neck = ["B", "E", "A", "D", "G", "C", "F"]
  accidental = ["#", "b"]

  def search_keyboard(search_note): 
    #what number is the keyboard on?
    for j, note in Question.on_keyboard.items():
      if search_note in note:
        return j

  def numOnCircle(): 
    #choose a key on circle and find its number of accidentals
    n = random.randint(-7, 7)

    #if there are keys to choose from
    if type(Question.circ[n]) == list:
      ww = random.randint(0, 1)
      start_note = Question.circ[n][ww]
    else:
      start_note = Question.circ[n]

    first_loc = Question.search_keyboard(start_note)

    #start_note is the key, n is the number of accidentals, j is the location of the first note in the key on the keyboard
    return start_note, first_loc, n

  def check_user_input(user_input, answer):
    if user_input == answer:
      print("here is answer", answer)
      print("CORRECT")
    else:
      print("here is answer", answer)
      print("WRONG")

  def check_user_input_enharmonic(user_input, answer):
    #get the int value of keyboard position
    keyboard_input = Question.return_keyboard_position(user_input.split("-"))
    keyboard_answer = Question.return_keyboard_position(answer.split("-"))
    if keyboard_input == keyboard_answer:
      print("here is answer", answer)
      print("CORRECT")
      return True
    else:
      print("here is answer", answer)
      print("WRONG")
      return False

  def return_keyboard_position(split_answer):
    keyboard_answer = []
    for note in split_answer:
      for int_position, key in Question.on_keyboard.items():
        if note == key:
          keyboard_answer.append(int_position)
          break
    return keyboard_answer
class Scale_Question(Question):

  possible_inputs = ['C', 'B#', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'Fb', 'F', 'E#', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', "Cb", " "]

  def __call__(self):
    show, answer = self.create()
    print(f"write the scale of {show}M") #include
    user_guess = self.inp()
    Question.check_user_input_enharmonic(user_guess, answer)

  def create(self):
    #of, j, n = numOnCircle() #i dont want j but if i dont get it it will be with of
    start_note, first_loc, n = Question.numOnCircle()

    clean_letter = start_note[0] #look at letter, not accidental
    numb = Question.key_lett.index(clean_letter)

    little = []
    #iterate through letters and append letters in a fashion that key letter is at front
    for i in list(range(len(Question.key_lett))):
      numb %= 7
      little.append(Question.key_lett[numb])
      numb += 1

    #eyeOn is all the notes that will have the accidental
    if n >= 0:
      eyeOn = Question.neck[(7-n):]
    else:
      eyeOn = Question.neck[:n*(-1)]
    #right side of circle is positive, left is negative
    if n >= 0:
      add = "#"
    else:
      add = "b"

    answer = [x + add if x in eyeOn else x for x in little]
    answer = "-".join(answer)
    #create the scale
    """
    for i in little: 
      if i in eyeOn:
        w = little.index(i)
        little[w] += add

    return start_note, little
    """
    return start_note, answer

  def inp(self):
    guess = input("Answer: ").strip()
    while (Scale_Question.bad_input(guess.split("-"))):
      print("case sensitive, beware the letters you type")
      guess = input("Answer: ").strip()
    return guess

  def bad_input(guess):
    for i in guess:
      if i not in Scale_Question.possible_inputs:
        return True
    else:
      return False
class Interval_Question(Question):
  possible_inputs = ["m2", "M2", "m3", "M3", "P4", "aug4, d5, TT", "P5", "m6", "M6", "m7", "M7", "P8"]

  #basically overloading the () operator
  def __call__(self):
    #create the question
    answer, start_note, end_note = self.create()
    #print question
    print(f"Find the interval of {start_note} - {end_note}")
    #receive appropriate input from the user
    user_guess = Interval_Question.inp()
    #assess its correctness and print a message
    Question.check_user_input(user_guess, answer)

  def create(self):
    #select an interval to work with
    #inte is the name of the interval
    i = random.randint(0, 11)
    inte = Question.intervals[i]
    true_distance = i+1

    #start_note is the key, first_loc is the location of the first note in the key on the keyboard, n is the number of accidentals,
    start_note, first_loc, n = Question.numOnCircle() 
    #in this function we dont do anything with n

    position = (first_loc + true_distance) % 12
    end_note = Question.on_keyboard[(position)] #by mod 12 instead of 11, C is always 0

    #start_note is the first note in the interval
    #end_note is the second not for the interval

    #if there are options
    q = random.randint(0,1)
    if type(end_note) is list:
      end_note = end_note[q]

    #inte is the name of the interval
    return inte, start_note, end_note

  def inp():
    guess = input("Answer: ").strip() #could [have tried repetitive inputs with a list] [split at "-" instead of " "]

    while (guess not in Interval_Question.possible_inputs):
      print("case sensitive, beware the letters you type")
      guess = input("Answer: ").strip()

    return guess
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
