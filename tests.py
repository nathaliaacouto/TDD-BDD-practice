#Arquivo de testes
#Alunos:
# Nathália Couto (nvc@cesar.school)
# Miguel Cabral (mcc2@cesar.school)

from main import Calculator, CalculadoraErro
import pytest

@pytest.mark.parametrize("a,b,res",
                         [(5,2,7),
                         (3,6,9),
                         (5.2, 2, 7.2)])
def test_soma(a,b,res):
    calculadora = Calculator()
    res_calc = calculadora.soma(a,b)
    assert res == res_calc
    

@pytest.mark.parametrize("a,b,res",
                         [(10,20,-10),
                         (3,6,-3),
                         (5.2,2,3.2)])
def test_sub(a,b,res):
  calculadora = Calculator()
  res_calc = calculadora.sub(a,b)
  assert res == res_calc


@pytest.mark.parametrize("a,b,res",
                         [(5,2,10),
                         (3,6,18),
                         (5.2,2,10.4)])
def test_multi(a,b,res):
    calculadora = Calculator()
    res_calc = calculadora.multi(a,b)
    assert res == res_calc


@pytest.mark.parametrize("a,b,res",
                         [(5,2,2.5),
                         (-3,6,0.5),
                         (10,2,5),
                         (10,0,0)])

def test_divisao(a, b, res):
  calculadora = Calculator()
  res_calc = calculadora.divisao(a,b)
  assert res == res_calc

@pytest.mark.parametrize("a,b,res",
                         [(5,2,25),
                         (-3,6,2),
                         (10,2,100)])

def test_potencia(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.potencia(a,b)
    assert res == res_calc


@pytest.mark.parametrize("a,b,res",
                        [("5",2,7),
                         (5,"2",7),
                         ("5","2","7")])
def test_soma_tipos(a,b,res):
    calculadora = Calculator()
    with pytest.raises(CalculadoraErro):
        res_calc = calculadora.soma(a, b)

@pytest.mark.parametrize("a,b,res",
                        [("5",2,7),
                         (5,"2",7),
                         ("5","2","7")])
def test_sub_tipos(a,b,res):
    calculadora = Calculator()
    with pytest.raises(CalculadoraErro):
        res_calc = calculadora.sub(a, b)

@pytest.mark.parametrize("a,b,res",
                        [("5",2,7),
                         (5,"2",7),
                         ("5","2","7")])
def test_multi_tipos(a,b,res):
  calculadora = Calculator()
  with pytest.raises(CalculadoraErro):
    res_calc = calculadora.multi(a, b)

@pytest.mark.parametrize("a,b,res",
                        [("5",2,7),
                         (5,"2",7),
                         ("5","2","7")])
def test_divisao_tipos(a,b,res):
  calculadora = Calculator()
  with pytest.raises(CalculadoraErro):
    res_calc = calculadora.divisao(a, b)

@pytest.mark.parametrize("a,b,res",
                        [("5",2,7),
                         (5,"2",7),
                         ("5","2","7")])
def test_potencia_tipos(a,b,res):
  calculadora = Calculator()
  with pytest.raises(CalculadoraErro):
    res_calc = calculadora.potencia(a, b)

@pytest.mark.parametrize("a,b,res",
                         [(3,5,-2)])
def test_res_natural_sub(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.sub(a,b)
    assert res_calc > 0

@pytest.mark.parametrize("a,b,res",
                         [(1000,2000,3000)])
def test_res_natural_soma(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.soma(a,b)
    assert res_calc > 0

@pytest.mark.parametrize("a,b,res",
                         [(0,0,0)])
def test_res_natural_mult(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.multi(a,b)
    assert not res_calc < 0

@pytest.mark.parametrize("a,b,res",
                         [(5,5,1)])
def test_res_natural_divi(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.divisao(a,b)
    assert res_calc > 0

@pytest.mark.parametrize("a,b,res",
                         [(2,1000,100)])
def test_res_natural_pot(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.potencia(a,b)
    assert res_calc > 0