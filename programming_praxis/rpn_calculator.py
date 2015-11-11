import string
import collections


class Calculator:

  def __init__(self):
    self.__ops = {'+': self.__add,
                  '/': self.__div, 
                  '*': self.__mul,
                  '^': self.__pow, 
                  '-': self.__sub}

    self.__deque = collections.deque()

    self.__start()

  def __add(self, x, y):
    return x + y

  def __clr(self):
    self.__deque.clear()

  def __div(self, x, y):
    return x / float(y)

  def __eval(self, exp):
    tokens = exp.split()

    for token in tokens:
      try:
        token = float(token)
      except ValueError:
        if token not in self.__ops:
          raise KeyError
        if len(self.__deque) < 2:
          raise IndexError
        rhs = self.__deque.pop()
        lhs = self.__deque.pop()
        token = self.__ops[token](lhs, rhs)

      self.__deque.append(token)

    # return the buffer so the user can see it (not in the spec)
    if len(self.__deque) != 1:
      return list(self.__deque)

    return self.__deque[0]

  def __mul(self, x, y):
    return x * y

  def __pow(self, x, y):
    return x ** y

  def __repl(self):
    while True:
      exp = raw_input('>>> ')

      if len(exp) == 0:
        continue

      if exp == 'c':
        self.__clr()
      else:
        try:
          print self.__eval(exp)
        except IndexError:
          print 'Error: Not enough operands.'
        except KeyError:
          print 'Error: Invalid token.'

  def __start(self):
    self.__repl()

  def __sub(self, x, y):
    return x - y


if __name__ == '__main__':
  c = Calculator()