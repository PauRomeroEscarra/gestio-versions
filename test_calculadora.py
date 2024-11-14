
from calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
       assert sumar(2, 3) == 5
       assert sumar(-1, 1) == 0
       assert sumar(0, 0) == 0
def test_restar():
       assert restar(3, 2) == 1
       assert restar(0, 0) == 0
       assert restar(5, 10) == -5

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 5) == -5
    assert multiplicar(0, 100) == 0

def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(5, 2) == 2.5
    assert dividir(0, 1) == 0
    assert dividir(1, 0) == "Error: No es pot dividir per zero."
