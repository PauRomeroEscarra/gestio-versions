
from calculadora import sumar, restar

def test_sumar():
       assert sumar(2, 3) == 5
       assert sumar(-1, 1) == 0
       assert sumar(0, 0) == 0
def test_restar():
       assert restar(3, 2) == 1
       assert restar(0, 0) == 0
       assert restar(5, 10) == -5
