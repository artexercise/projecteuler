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

def test_e1_a():
    if not testitem_FunctionTest(e1_a, 10, 23): return
    print("Passed: e1_a")

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
test_e1_a()
print("  Result of Function w/ Input 10: {}".format(e1_a(10)))
print("Result of Function w/ Input 1000: {}".format(e1_a(1000)))

t10 = timeit.timeit(stmt='e1_a(10)', setup='from __main__ import e1_a', number=1000)
t1000 = timeit.timeit(stmt='e1_a(1000)', setup='from __main__ import e1_a', number=1000)
print("  Function Time Run 1000 times w/ Input 10: {}".format(t10))
print("Function Time Run 1000 times w/ Input 1000: {}".format(t1000))