import random,json,time

def load_question():
    with open("questions.json","r") as f:
        questions = json.load(f);

    return questions

def get_random_question(questions,total_question):
    if total_question >len(questions):
        total_question = len(questions)
    questions = random.sample(questions,total_question)

    return questions

def ask_question(question):
    print(question["question"])
    print("A",question["A"])
    print("B",question["B"])
    print("C",question["C"])
    print("D",question["D"])

    while True:
        answer = (input("Choose the correct answer : ")).upper()
        if answer not in ("A","B","C","D"):
            print("Invalid answer,Try again!")
            continue
        elif question["answer"] == answer:
            return True
        else:
            break
        
    return False

def main():
    questions = load_question()
    total_questions = int(input("Total number of questions : "))
    random_question = get_random_question(questions,total_questions)
    correct  = 0
    start_time = time.time()

    for question in random_question:
        is_correct = ask_question(question)
        if is_correct:
            correct = correct+1

        print("---------------------------------------------------------------")

    total_time = time.time() - start_time

    print("Summary")
    print("Total number of question asked :",len(random_question))
    print("Correct answers :",correct)
    print("Score :", str(round((correct/len(random_question)) * 100,2))+"%")
    print("Time :", round(total_time,2),"seconds")

if __name__ == "__main__":
    main()






