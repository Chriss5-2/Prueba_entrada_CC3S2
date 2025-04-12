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
    questions = [Question("¿Cuánto es 35x6?", ["180", "210", "240", "220"], "2"), # Question 1
    Question("¿Cuál es la capital de Austria?", ["Lima", "Viena", "Bruselas", "Dhaka"], "2"), # Question 2
    Question("¿De qué colores es la bandera de Japón?",["Blanca y roja", "Azul y amarillo", "Celeste, blanco y amarillo", "Negro, amarillo y rojo"],"1"), # Question 3
    Question("¿Qué juego ganó el GOTY el año 2024?", ["God Of War Ragnarok", "Ghost of Tsushima", "Astro Bot", "The last of us II"], "3"), # Question 4
    Question("¿Quién escribió el Caballero Carmelo?", ["Cesar Acuña", "Mario Vargas Llosa", "Abraham Valdemolar", "Ciro Alegria"], "3"), # Question 5
    Question("¿Qué canción NO es de Juan Gabriel?", ["Así fue", "Hasta que te conocí", "Porque me haces llorar", "Waka Waka"], "4"), # Question 6
    Question("¿Cuál es un color primario", ["Verde", "Rojo", "Blanco", "Morado"], "2"), # Question 7
    Question("¿Qué palabra NO tiene tres sílabas", ["Recuerda", "Cabello", "Héroe", "Aumento"], "3"), # Question 8
    Question("¿Qué año se fundó la Universidad Nacional de Ingeniería (UNI)?", ["1876", "1856", "1866", "NA"], "1"), # Question 9
    Question("¿Qué profesor enseña Desarrollo de Software en el periodo 2025-1 en la UNI?", ["Pablo Lopez", "Marco Alania", "Yuri Ccoica", "Cesar Lara"], "4")] # Question 10
    #Add questions one by one
    #quiz.add_question(question1) quiz.add_question(question2) quiz.add_question(question3) quiz.add_question(question4)
    #Add all questions at the same time
    for q in questions:
        quiz.add_question(q)
    #Create question
    question = quiz.get_next_question()
    #Show questions
    while question != None:
        print("---------------------------------------------")
        print(question.description)
        for i, option in enumerate(question.options,1):
            print(str(i)+") "+option) #Use str(i) because i is an integer variable and question is a string variable
        answer = input("Ingrese la alternativa correcta: ")
        #Choose a alternative of the range
        while answer not in ["1","2","3","4"]:
            #Choose another alternative if the answer is out the range or if is None
            print("Please choose an option between 1 and 4")
            print(question.description)
            for i, option in enumerate(question.options,1):
                print(str(i)+") "+option)
            print(question.description)
            answer = input("Ingrese la alternativa correcta: ")
        #Correct Answer
        if quiz.answer_question(question, answer):
            print("Correct Answer!!!! Congratulations :D")
        #Incorrect Answer
        elif not quiz.answer_question(question, answer):
            print("Incorrect Answer ;( The correct answer is the alternative "+question.correct_answer)

        question = quiz.get_next_question()
    print("---------------------------------------------")
    print("Juego terminado")
    print("Puntuacion: ")
    print("- " + str(quiz.correct_answers) + " preguntas correctas")
    print("- " + str(quiz.incorrect_answers) + " preguntas incorrectas")

if __name__ == "__main__":
    run_quiz()

