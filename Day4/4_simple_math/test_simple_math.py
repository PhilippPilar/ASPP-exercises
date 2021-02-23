from simple_math import *


def test_simple_add():
	assert simple_add(3,4) == 7
	assert simple_add(-2,7) == 5

def test_simple_sub():
	assert simple_sub(7,5) == 2
	assert simple_sub(7,-3) == 10
	
def test_simple_mult():
	assert simple_mult(3,7) == 21
	assert simple_mult(-2,3) == -6
	assert simple_mult(-2,-2) == 4
	
def test_simple_div():
	assert simple_div(21,7) == 3
	assert simple_div(21,-7) == -3
	assert simple_div(-6,-3) == 2

def test_poly_first():
	assert poly_first(2,3,4) == 11
	assert poly_first(-1,3,4) == -1

def test_poly_second():
	assert poly_second(2,3,4,5) == 31
	assert poly_second(-1,3,4,5) == 4