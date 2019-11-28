from question import Question
import random
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
