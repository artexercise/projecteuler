import timeit

def e1_a(limit):
	'''
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.
	'''
	sum = 0
	for x in range(0,limit):
		if x%3 == 0 or x%5 == 0:
			sum = sum + x
	return sum

def e1_b(limit):
	'''
	Trying the same thing with a generator for speed check.  Using the website below to help set up.
	https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
	'''
	sum = 0
	for x in get3or5(1):
		if x < limit:
			sum = sum + x
		else:
			return sum

def e1_c(limit):
	'''
	'''
	sum = 0
	for x in range(0,limit):
		sum += x if x%3 == 0 or x%5 == 0 else 0
	return sum
			
def get3or5(n):
	while True:
		if n%3 == 0 or n%5 == 0:
			yield n
		n = n + 1

def test_e1_a():
    if not testitem_FunctionTest(e1_a, 10, 23): return
    print("Passed: e1_a")

def test_e1_b():
    if not testitem_FunctionTest(e1_b, 10, 23): return
    print("Passed: e1_b")

def test_e1_c():
    if not testitem_FunctionTest(e1_c, 10, 23): return
    print("Passed: e1_c")

def testitem_FunctionTest(inFunc, inArg, outResult):
    try:
        assert inFunc(inArg)==outResult
        return True
    except AssertionError:
        print(" -*: Failed: {2}({0}) != {1}".format(inArg, outResult, inFunc.__name__))
        return False

# -=-=- -=-=- -=-=- -=-=- -=-=-
# Test Functions
# -=-=- -=-=- -=-=- -=-=- -=-=-
print("--=-- --=-- --=-- --=-- --=--")
print("--=-- --=-- e1_a  --=-- --=--")
print("--=-- --=-- --=-- --=-- --=--")
test_e1_a()
print("  Result of Function w/ Input 10: {}".format(e1_a(10)))
print("Result of Function w/ Input 1000: {}".format(e1_a(1000)))

t10 = timeit.timeit(stmt='e1_a(10)', setup='from __main__ import e1_a', number=1000)
t1000 = timeit.timeit(stmt='e1_a(1000)', setup='from __main__ import e1_a', number=1000)
print("  Function Time Run 1000 times w/ Input 10: {}".format(t10))
print("Function Time Run 1000 times w/ Input 1000: {}".format(t1000))

print("--=-- --=-- --=-- --=-- --=--")
print("--=-- --=-- e1_b  --=-- --=--")
print("--=-- --=-- --=-- --=-- --=--")
test_e1_b()
print("  Result of Function w/ Input 10: {}".format(e1_b(10)))
print("Result of Function w/ Input 1000: {}".format(e1_b(1000)))

t10 = timeit.timeit(stmt='e1_b(10)', setup='from __main__ import e1_b', number=1000)
t1000 = timeit.timeit(stmt='e1_b(1000)', setup='from __main__ import e1_b', number=1000)
print("  Function Time Run 1000 times w/ Input 10: {}".format(t10))
print("Function Time Run 1000 times w/ Input 1000: {}".format(t1000))

print("--=-- --=-- --=-- --=-- --=--")
print("--=-- --=-- e1_c  --=-- --=--")
print("--=-- --=-- --=-- --=-- --=--")
test_e1_c()
print("  Result of Function w/ Input 10: {}".format(e1_c(10)))
print("Result of Function w/ Input 1000: {}".format(e1_c(1000)))

t10 = timeit.timeit(stmt='e1_c(10)', setup='from __main__ import e1_c', number=1000)
t1000 = timeit.timeit(stmt='e1_c(1000)', setup='from __main__ import e1_c', number=1000)
print("  Function Time Run 1000 times w/ Input 10: {}".format(t10))
print("Function Time Run 1000 times w/ Input 1000: {}".format(t1000))