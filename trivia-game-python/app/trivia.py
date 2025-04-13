from random import *

class Question:
    def __init__(self, description, options, correct_answer, level):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
        self.level = level

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

    def del_question(self, question):
        self.questions.remove(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def get_question_by_level(self, level):
        index = randin(0,len(self.questions))
        while questions[index].level != level:
            index = randin(0,len(self.questions))
        question = self.questions[index]
        return question

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers+=1
            return True
        else:
            self.incorrect_answers+=1
            return False

    def get_question_level(self, question)
        return question.level

def run_quiz():
    Rendimiento = 0
    num_preguntas = 0
    puntos = 0
    level = 1
    print("Bienvenido al juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta")

    quiz = Quiz()
# REPOSITORIOS DE PREGUNTAS
    # Preguntas de dificultad 1
    questions = [Question("¿Cuál es el planeta más cercano al Sol", ["Mercurio", "Marte", "Tierra", "Jupiter"], "1", 1), # Question 1
    Question("¿Cuántas patas tiene una araña?", ["6", "9", "8", "7"], "3", 1), # Question 2
    Question("¿Qué día se celebra la Navidad?", ["31 de diciembre", "25 de diciembre", "1 de enero", "24 de noviembre"], "2", 1), # Question 3
    Question("¿Qué juego ganó el GOTY el año 2024?", ["God Of War Ragnarok", "Ghost of Tsushima", "Astro Bot", "The last of us II"], "3", 1), # Question 4
    Question("¿Cuántos dedos tiene una mano humana?", ["Cinco", "Cuatro", "Diez", "Seis"], "1", 1), # Question 5
    Question("¿Qué canción NO es de Juan Gabriel?", ["Así fue", "Hasta que te conocí", "Porque me haces llorar", "Waka Waka"], "4", 1), # Question 6
    Question("¿Cuál es un color primario", ["Verde", "Rojo", "Blanco", "Morado"], "2", 1), # Question 7
    Question("¿Qué animal hace 'miau'?", ["Perro", "Vaca", "Gato", "Pájaro"], "3", 1), # Question 8
    Question("¿Qué fruta es amarilla por fuera y blanca por dentro?", ["Manzana", "Plátano", "Pera", "Papaya"], "2", 1) # Question 9
    Question("¿En qué país está la Torre Eiffel?", ["España", "Italia", "Francia", "Alemania"], "3", 1) # Question 10
    # Preguntas de dificultad 2
    Question("¿Cuál es la capital de Austria?", ["Lima", "Viena", "Bruselas", "Dhaka"], "2", 2),
    Question("¿Qué palabra NO tiene tres sílabas", ["Recuerda", "Cabello", "Héroe", "Aumento"], "3", 2),
    Question("¿Qué año se fundó la Universidad Nacional de Ingeniería (UNI)?", ["1876", "1856", "1866", "NA"], "1", 2),
    Question("¿Quién escribió 'Cien años de soledad'?", ["Pablo Neruda", "Gabriel García Márquez", "Mario Vargas Llosa", "Julio Cortázar"], "2", 2)
    Question("¿Cuál es la capital de Japón?", ["Pekín", "Tokio", "Seúl", "Bangkok"], "2", 2)
    Question("¿Qué elemento químico tiene el símbolo Hg?", ["Helio", "Hidrógeno", "Hierro", "Mercurio"], "4", 2),
    Question("¿En qué continente está Egipto?", ["Asia", "Europa", "África", "Oceanía"], "3", 2),
    Question("¿Cuántos lados tiene un icoságono?", ["Veinte", "Diesciseis", "Veinticuatro", "Diez"], "1", 2),
    Question("¿Qué órgano del cuerpo humano bombea sangre?", ["Pulmón", "Hígado", "Riñón", "Corazón"], "4", 2),
    Question("¿Cuál es el idioma más hablado del mundo?", ["Español", "Inglés", "Chino mandarín", "Hindi"], "3", 2),
    # Preguntas de dificultad 3
    Question("¿Quién escribió el Caballero Carmelo?", ["Cesar Acuña", "Mario Vargas Llosa", "Abraham Valdemolar", "Ciro Alegria"], "3", 3),
    Question("¿Cuál es el número atómico del oxígeno?", ["6", "7", "8", "9"], "3", 3),
    Question("¿Qué obra escribió Miguel de Cervantes?", ["La Odisea", "Don Quijote de la Mancha", "Hamlet", "El Principito"], "2", 3),
    Question("¿Qué filósofo dijo 'Solo sé que nada sé'?", ["Platón", "Aristóteles", "Descartes", "Sócrates"], "4", 3),
    Question("¿Qué científico formuló la teoría de la relatividad?", ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"], "3", 3),
    Question("¿Qué hueso protege el cerebro?", ["Fémur", "Columna", "Cráneo", "Húmero"], "3", 3),
    Question("¿En qué año se firmó la independencia de EE.UU.?", ["1776", "1492", "1810", "1865"], "1", 3),
    Question("¿Qué juego ganó el GOTY el año 2024?", ["God Of War Ragnarok", "Ghost of Tsushima", "Astro Bot", "The last of us II"], "3", 3),
    Question("¿Cuánto es 2^(2^2)", ["64", "128", "16", "32"], "3", 3),
    Question("¿Quién pintó 'La noche estrellada'?", ["Claude Monet", "Vincent van Gogh", "Pablo Picasso", "Salvador Dalí"], "2", 3)]
    #Add questions one by one
    #quiz.add_question(question1) quiz.add_question(question2) quiz.add_question(question3) quiz.add_question(question4)
    #Add all questions at the same time
    for q in questions:
        quiz.add_question(q)

    #Show questions
    while num_preguntas < 10: #question.current_question_index < 10:
        if num_preguntas > 0:
            print("---------------------------------------------")
            print("Pregunta número "+str(num_preguntas+1)+" - Nivel "+level)
        else:
            print("Pregunta número 1 - Nivel 1")
        question = quiz.get_question_by_level(level)
        #question = quiz.get_next_question()
        #print("---------------------------------------------")
        print(question.description)
        # Mostrar opciones
        for i, option in enumerate(question.options,1):
            print(str(i)+") "+option) #Use str(i) because i is an integer variable and question is a string variable
        answer = input("Ingrese la alternativa correcta: ")
        # SELECCION DE ALTERNATIVAS
        #Choose a alternative of the range
        while answer not in ["1","2","3","4"]:
            #Choose another alternative if the answer is out the range or if is None
            print("Please choose an option between 1 and 4")
            print(question.description)
            for i, option in enumerate(question.options,1):
                print(str(i)+") "+option)
            print(question.description)
            answer = input("Ingrese la alternativa correcta: ")
        #El resultado de la respuesta lo guardamos en una variable
        correct_answer = quiz.answer_question(question, answer)
        if correct_answer: #quiz.answer_question(question, answer):
            print("Correct Answer!!!! Congratulations :D")
            puntaje += 2
            #num_preguntas++
            #quiz.del_question(question)
        #Incorrect Answer
        elif not correct_answer:
            print("Incorrect Answer ;( The correct answer is the alternative "+question.correct_answer)
            if puntaje > 0:
                puntaje -= 1
        num_preguntas++
        quiz.del_question(question)
        if quiz.correct_answers > 6:
            level = 3
        elif quiz.correct_answers >= 3 and quiz.correct_answers <= 6:
            level = 2
        else:
            level = 1

    print("---------------------------------------------")
    print("Juego terminado")
    print("Puntuación: ")
    print("- " + str(quiz.correct_answers) + " preguntas correctas")
    print("- " + str(quiz.incorrect_answers) + " preguntas incorrectas")
    print("- " + str(puntaje*5) + " puntos")

if __name__ == "__main__":
    run_quiz()

