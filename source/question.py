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
