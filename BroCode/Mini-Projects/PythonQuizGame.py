questions = (
  "How many elements are in the periodic table?: ", 
  "Which animal lays the largest eggs?: ", 
  "How many bones are there in the human body?: ", 
  "What is the most abundant gas in Earth's atmosphere?: ", 
  "Which planet in solar system is the hottest?: "
)

options = (
  ("A. 116", "B. 120", "C. 118", "D. 114"), 
  ("A. Whale", "B. Elephant", "C. Ostrich", "D. Emu"), 
  ("A. 204", "B. 205", "C. 206", "D. 208"), 
  ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"), 
  ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "C", "C", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("--------------------")
  print(question)

  for option in options[question_num]:
    print(option)
  
  guess = input("Enter (A, B, C, D):").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("CORRECT")
  else:
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")

  question_num += 1

print("--------------------")
print("       RESULTS      ")
print("--------------------")

print("answers: ", end="")
for answer in answers:
  print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
  print(guess, end=" ")
print()

score = int(score/len(questions) * 100)
print(f"Your score is: {score}%")

