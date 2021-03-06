import timeit

def e2_a(limit):
	'''
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
    find the sum of the even-valued terms.
	'''
	n1 = 1
	n2 = 1
	n3 = 0
	sum = 0
	while n1 < limit or n2 < limit:
		n3 = n1 + n2
		if n3 < limit and n3 % 2 == 0:
			sum = sum + n3
		n1 = n2
		n2 = n3
	return sum

def test_e2_a():
    if not testitem_FunctionTest(e2_a, 10, 10): return
    print("Passed: e2_a")

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
print("--=-- --=-- e2_a  --=-- --=--")
print("--=-- --=-- --=-- --=-- --=--")
test_e2_a()
print("  Result of Function w/ Input 10: {}".format(e2_a(10)))
print("Result of Function w/ Input 1000: {}".format(e2_a(4000000)))

t10 = timeit.timeit(stmt='e2_a(10)', setup='from __main__ import e2_a', number=1000)
t1000 = timeit.timeit(stmt='e2_a(4000000)', setup='from __main__ import e2_a', number=1000)
print("     Function Time Run 1000 times w/ Input 10: {}".format(t10))
print("Function Time Run 1000 times w/ Input 4000000: {}".format(t1000))
