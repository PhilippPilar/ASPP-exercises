"""
A collection of simple math operations
"""

def simple_add(a,b):
	"""
	Add two numbers a,b.
	
	Parameters
	----------
	a : scalar
	b : scalar
	
	Examples
	--------
	simple_add(2,3) = 5
	"""
	return a+b

def simple_sub(a,b):
	"""
	Subtract a from b.
	
	Parameters
	----------
	a : scalar
	b : scalar
	
	Examples
	--------
	simple_sub(5,3) = 2
	"""
	return a-b

def simple_mult(a,b):
	"""
	Multiply a with b.
	
	Parameters
	----------
	a : scalar
	b : scalar
	
	Examples
	--------
	simple_mult(5,3) = 15
	"""
	return a*b

def simple_div(a,b):
	"""
	Divide a by b.
	
	Parameters
	----------
	a : scalar
	b : scalar
	
	Examples
	--------
	simple_div(9,3) = 3
	"""
	return a/b

def poly_first(x, a0, a1):
	"""
	Returns value of first order polynomial a0 + a1*x
	
	Parameters
	----------
	a0 : scalar
	a1 : scalar
	x : scalar
	
	Examples
	--------
	poly_first(1,5,3) = 8
	"""
	return a0 + a1*x

def poly_second(x, a0, a1, a2):
	"""
	Returns value of second order polynomial a0 + a1*x + a2*x**2
	
	Parameters
	----------
	a0 : scalar
	a1 : scalar
	a2 : scalar
	x : scalar
	
	Examples
	--------
	poly_second(1,5,3,2) = 10
	"""
	return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
