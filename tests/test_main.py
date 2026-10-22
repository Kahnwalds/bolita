import pytest
from main import calcular_area_triangulo

def test_area_triangulo():
    #Resultado real
    actual_result = calcular_area_triangulo(13, 3)

    #assert (asegurando o verificando) que el resultado actual
    #sea igual que el expected result
    assert actual_result == pytest.approx(19.5, abs=0.01)

    