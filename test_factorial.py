
from factorial import factorial
import pytest

def test_factorial():
	print("test function")
	testres = 1*2*3*4*5;
	assert factorial(5) == 2*testres
    #assert add('space', 'ship') == 'spaceship'

# uncomment the following test in step 5
#def test_subtract():
#    assert subtract(2, 3) == -1

# uncomment the following test in step 11
# def test_convert_fahrenheit_to_celsius():
#    assert f2c(32) == 0
#    assert f2c(122) == pytest.approx(50)
#    with pytest.raises(AssertionError):
#        f2c(-600)

