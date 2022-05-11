"""
DIRECTIONS
Prompt boils down to solve the system of equations and figure out the minimum value of x to make a larger than b.
Note the initial value of a is always smaller than or equal to b.
y = a * 3^x
y = b * 2^x

--------------------------

EQUATION SOLVING:
    y = a * 3^x
    y = b * 2^x

    a * 3^x = b * 2^x
    ln(a * 3^x) = ln(b * 2^x)

    ln(a) + ln(3^x) = ln(b) + ln(2^x)
    ln(a) + xln(3) = ln(b) + xln(2)

    xln(3) - xln(2) = ln(b) - ln(a)
    x(ln(3) - ln(2)) = ln(b/a)
    x(ln(3/2)) = ln(b/a)

    x = ln(b/a) / ln(3/2)
    x = log 3/2 of b/a

    x simply represents the time when the two bears are the same weight.
    Because of this, ciel() will give us the first integer x must equal for a to be greater than b.
    However, this does not apply to when x is an integer itself.

    To combat this fact, we must either add a condition to check whether x is an integer, or
    do the easier option of adding one to x and rounding all of that down.


"""
import math

# Parse user input.
userInput = input().split(' ')
a = float(userInput[0])
b = float(userInput[1])

# Math expression from above.
answer = math.log(b / a, 3.0 / 2)
answer = math.floor(answer + 1)

print(answer)
