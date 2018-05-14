#!/usr/local/bin/python
# coding: latin-1
import math
import sys

def funcaoA(flag, x):
	if flag:
		return -math.atan(x-1)

	return x + math.atan(x-1)


def funcaoB(flag, x):
	e = math.exp(1)
	if flag:
		return (((e**x)*(x**(5.0/3.0)))/9.0)**(1.0/2.0)
	return 9 * (x ** (1/3)) - e**x

def funcaoC(flag, x):
	e = math.exp(1)
	if flag:
		return (math.log(6.0*math.log(x,e),e))/math.log(2,e)
	return 2**x - 6.0*math.log(x,e)


def funcaoIteracao(func, x_ite, x_abs):
	print('{:^9}|{:^16}|{:^16}|{:^16}|{:^16}|'.format('iteracao', 'x', 'Eabs', 'Erel', 'f(x)'))

	i = 0

	while True:
		_x   = func(1, x_ite)
		fx   = func(0, _x)
		eabs = abs(_x - x_abs)
		erel = abs(_x - x_ite)/abs(_x)
		print('{:^9}|{:^16.12f}|{:^16.10f}|{:^16.12f}|{:^16.12f}|'.format(i, _x, eabs, erel, fx))

		if(eabs < 10**-15):
			break

		x_ite = _x
		i     = i + 1


def main(argv):
	arg = sys.argv

	if(len(arg) == 1):
		print("Duvidas? Use \"Help\" como passagem de parametro")
	else:
		if(arg[1] == 'a'):
			print('f(x) = x + arctg(x - 1)')
			x_abs = 0.479731007280
			funcaoIteracao(funcaoA, 2, x_abs)
		elif(arg[1] == 'b'):
			print('f(x) = 9*(x ** 1/3) - e ** x')
			x_abs = 0.001377422244
			funcaoIteracao(funcaoB, 1, x_abs)
		elif(arg[1] == 'c'):
			print('f(x) = 2**x - 6*ln(x)')
			x_abs = 2.377446269795246411
			funcaoIteracao(funcaoC, 2.5, x_abs)
		else:
			print('Implementacao trabalho pratico de Analise Numerica ANN0001-BCC/2018.1\n')
			print('Use como parametro na chamada do programa a funcao que deseja analisar:')
			print('    (a) f(x) = x + arctg(x - 1), partindo de x = 2')
			print('    (b) f(x) = 9*(x ^ 1/3) - e ** x, partindo de x = 1')
			print('    (c) f(x) = 2^x - 6*ln(x), partindo de x = 2')
			return 0


if __name__ == "__main__":
    main(sys.argv)
