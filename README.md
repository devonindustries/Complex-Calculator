# Complex Calculator
 A calculator for performing complex arithmetic. Contains one class called 'Complex', which takes two arguments primarily.

 To create a complex number, say 1+i, we would write Complex(1,1). Arithmetic with complex numbers in this module is defined in the usual way, so to add complex numbers, all we need to write is

 ```
Complex(1,0) + Complex(0,1)
```

Which would return `Complex(1,1)`, or as a string, `'1+i'`. We can also perform other operations on complex numbers, such as subtraction, multiplication and division, which work in the same manner.

We can also perform other operations, such as raising to powers. For now, the calculator only supports powers in the form of real numbers, but support for complex power notation may come in a later version. This uses De-Moivre's theorem to calculate precisely. We may also invert a complex number somply by raising it to the power of `-1`.

There are a number of built in methods that can be applied to complex numbers. For example, we may return the conjugate of a complex number by `Complex(1,1).conjugate()`, which would return `Complex(1,-1)`, and the `.mod_arg()` method which returns a tuple containing the modulus and argument of the complex number respectively.

The argument `.arg()` returns the argument of the complex number alone, and the modulus of the complex number may be obtained by using `abs(Complex(...))`.

In terms of comparison operators, for example evaluating the inequality `Complex(2,3) < Complex(5,12)`, the calculator will compare the moduli of the two complex numbers. In this instance, we have `5 < 13`, which evaluates to `True`.