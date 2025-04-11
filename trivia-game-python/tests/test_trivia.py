import pytest
from app.trivia import Question

def test_question_correct_answer():
    question = Question("¿Qué juego ganó el GOTY el año 2024?", ["Astro Bot", "God of War Ragnarok", "The Last of Us 2", "Ghost of Tsushima"], "1")
    assert question.is_correct("1")

def test_question_incorrect_answer():
    question = Question("¿Qué juego ganó el GOTY el año 2024?", ["Astro Bot", "God of War Ragnarok", "The Last of Us 2", "Ghost of Tsushima"], "1")
    assert not question.is_correct("2")

def test_question_invalid_answer():
    question = Question("¿Qué juego ganó el GOTY el año 2024?", ["Astro Bot", "God of War Ragnarok", "The Last of Us 2", "Ghost of Tsushima"], "1")
    assert not question.is_correct("5")

def test_question_incorrect_type_input():
    question = Question("¿Qué juego ganó el GOTY el año 2024?", ["Astro Bot", "God of War Ragnarok", "The Last of Us 2", "Ghost of Tsushima"], "1")
    assert not question.is_correct(2)

def test_question_empty_answer():
    question = Question("¿Qué juego ganó el GOTY el año 2024?", ["Astro Bot", "God of War Ragnarok", "The Last of Us 2", "Ghost of Tsushima"], "1")
    assert not question.is_correct("")
