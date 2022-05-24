import math

# 1. Тест filter
is_even = lambda x: x % 2 == 0

seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def filtered(is_even, seq):
    filt = filter(is_even, seq)
    return list(filt)


b = filtered(is_even, seq)
print(b)

def test_filtered():
    assert filtered(is_even, seq) == [2, 4, 6, 8]


# 2. Тест map
seq2 = (5, 6, 7, 8, 9, 0, 3, 2, 1)
def summa (seq, seq2):
    result = map(lambda x, y: x+y, seq, seq2)
    return list(result)

c= summa (seq, seq2)
print(c)

def test_summa():
    assert summa(seq, seq2) == [6, 8, 10, 12, 14, 6, 10, 10, 10]

# 3. Тест sorted
def sort1(seq):
    result = sorted(seq2,reverse=True)
    return list(result)

d = sort1(seq2)
print(d)

def test_sort1():
    assert sort1(seq2) == [9, 8, 7, 6, 5, 3, 2, 1, 0]


# 4 Тест pi
print(math.pi)
def test_pi():
    assert math.pi == 3.141592653589793

# 5 Тест sqrt

print(math.sqrt(4))

def test_sqrt():
    assert math.sqrt(4)==2

# 6 Тест pow

print(pow(4,3))
def test_pow ():
    assert math.pow(4,3) == 64

# 7. Тест hypot

print(math.hypot(52,3))

def test_hypot():
    assert math.hypot(52,3)==52.08646657242167

