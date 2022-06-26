#Arquivo principal
#Alunos:
# Nathália Couto (nvc@cesar.school)
# Miguel Cabral (mcc2@cesar.school)

#Calculadora de números inteiros com:
# soma, subtração, divisão, multiplicação e potenciação

import pytest
import numbers

from tests import *

class CalculadoraErro(Exception):
  pass

class Calculator(object):
  def sub(self, a, b):
    self.check_natural(a)
    self.check_natural(b)

    self.check_less_zero(a)
    self.check_less_zero(b)

    self.check_type(a)
    self.check_type(b)
    return a-b

  def multi(self, a, b):
    self.check_natural(a)
    self.check_natural(b)

    self.check_less_zero(a)
    self.check_less_zero(b)

    self.check_type(a)
    self.check_type(b)
    return a*b

  def soma(self, a, b):
    self.check_natural(a)
    self.check_natural(b)

    self.check_less_zero(a)
    self.check_less_zero(b)

    self.check_type(a)
    self.check_type(b)
    return a+b

  def divisao(self, a, b):
    self.check_natural(a)
    self.check_natural(b)

    self.check_less_zero(a)
    self.check_less_zero(b)

    self.check_equal_zero(a)
    self.check_equal_zero(b)

    self.check_type(a)
    self.check_type(b)
    return a/b


  def potencia(self, a, b):
    self.check_natural(a)
    self.check_natural(b)

    self.check_less_zero(a)
    self.check_less_zero(b)

    self.check_type(a)
    self.check_type(b)
    return pow(a, b)

  def check_type(self,op):
    if not isinstance(op,numbers.Number):
      raise CalculadoraErro(f"{op} não é um número.")

  def check_natural(self,op):
    if not isinstance(op, int):
      raise CalculadoraErro(f"{op} não é um inteiro")

  def check_less_zero(self,op):
    if op < 0:
      raise CalculadoraErro(f"{op} é menor que zero")

  def check_equal_zero(self,op):
    if op == 0:
      raise CalculadoraErro(f"{op} é igual a zero")