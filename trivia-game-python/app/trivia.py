class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers+=1
            return True
        else:
            self.incorrect_answers+=1
            return False


def run_quiz():
    quiz = Quiz()
    question1 = Question("¿Cuánto es 35x6?", ["180", "210", "240", "220"], "2")
    question2 = Question("¿Cuál es la capital de Austria?", ["Lima", "Viena", "Bruselas", "Dhaka"], "2")
    question3 = Question("¿De qué colores es la bandera de Japón?",["Blanca y roja", "Azul y amarillo", "Celeste, blanco y amarillo", "Negro, amarillo y rojo"],"1")
    question4 = Question("¿Qué juego ganó el GOTY el año 2024?", ["God Of War Ragnarok", "Ghost of Tsushima", "Astro Bot", "The last of us II"], "3")
    #Add questions
    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)
    quiz.add_question(question4)
    #Create question
    question = quiz.get_next_question()
    #Show questions
    while question != None:
        print("---------------------------------------------")
        print(question.description)
        for i, option in enumerate(question.options,1):
            print(str(i)+") "+option) #Use str(i) because i is an integer variable and question is a string variable
        answer = str(input("Ingrese la alternativa correcta: "))
        #Choose a alternative of the range
        while answer not in ["1","2","3","4"]:
            #Choose another alternative if the answer is out the range or if is None
            print("Please choose an option between 1 and 4")
            print(question.description)
            for i, option in enumerate(question.options,1):
                print(str(i)+") "+option)
            print(question.description)
            answer = str(input("Ingrese la alternativa correcta: "))
        #Correct Answer
        if answer == question.correct_answer:
            print("Correct Answer!!!! Congratulations :D")
        #Incorrect Answer
        elif answer != question.correct_answer:
            print("Incorrect Answer ;( The correct answer is the alternative "+question.correct_answer)

        question = quiz.get_next_question()

if __name__ == "__main__":
    run_quiz()

