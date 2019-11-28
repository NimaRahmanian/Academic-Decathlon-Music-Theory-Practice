from question import Question
import random
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
