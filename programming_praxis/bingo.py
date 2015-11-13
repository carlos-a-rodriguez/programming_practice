import random


class Player():

  def __init__(self):
    self.__board = []
    self.__found = []

    for i in xrange(5):
      start = i * 15 + 1
      self.__board.append(random.sample(xrange(start, start + 15), 5))

    for i in xrange(5):
      self.__found.append([False] * 5)

    # middle cell is free
    self.__board[2][2] = 0
    self.__found[2][2] = True

  def __check_col(self, col):
    """Returns True if all numbers if column col have been called."""
    for i in xrange(5):
      if not self.__found[i][col]:
        return False

    return True

  def __check_diag(self, row, col):
    """Returns True if all numbers in the diagonal have been called."""
    if row == col:
      for i in xrange(5):
        if not self.__found[i][i]:
          return False
    else:
      for i in xrange(5):
        if not self.__found[i][5 - i - 1]:
          return False

    return True

  def __check_row(self, row):
    """Returns True if all the numbers if row row have been called."""
    for i in xrange(5):
      if not self.__found[row][i]:
        return False

    return True

  def check_win(self):
    """Returns True if Player has bingo."""
    for i in xrange(5):
      if self.__check_row(i):
        return True

    for i in xrange(5):
      if self.__check_col(i):
        return True

    if self.__check_diag(0,0):
      return True
    if self.__check_diag(0,4):
      return True

    return False

  def place_num(self, num):
    """Places a 'chip' on num if the player has it on the board."""
    row = (num - 1) / 15

    for i in xrange(5):
      if self.__board[row][i] == num:
        self.__found[row][i] = True

  def get_board(self):
    """Returns 2D list of tuples in the form (int, boolean) where the int
    is the number in the cell and the boolean is True if the number has been
    called."""
    board = []

    for i in xrange(5):
      board.append(zip(self.__board[i], self.__found[i]))

    return board


class Bingo:

  def __init__(self, num_players=1):
    self.__players = []

    for i in xrange(num_players):
      self.__players.append(Player())

    self.__nums = range(1, 76)
    random.shuffle(self.__nums)

  def __check_for_winner(self):
    """Returns True if at least one player has bingo."""
    for i in xrange(len(self.__players)):
      if self.__players[i].check_win():
        return True

    return False

  def __draw(self, num):
    """Places a 'chip' on each player's board if they have num on it."""
    for i in xrange(len(self.__players)):
      self.__players[i].place_num(num)

  def get_num_draws(self):
    """Returns the number of numbers drawn from the ball pool."""
    return 75 - len(self.__nums)

  def play(self):
    """Simulates a game of bingo until at least one person has won."""
    while not self.__check_for_winner():
      self.__draw(self.__nums.pop())


if __name__ == '__main__':
  # with one player, calculate the average number of numbers drawn before
  # bingo is called.
  count = 0

  for i in xrange(100):
    b = Bingo()
    b.play()
    count += b.get_num_draws()  

  print count / 1e2

  # with 500 players, calculate the average number of numbers drawn before
  # bingo is called.
  count = 0

  for i in xrange(100):
    b = Bingo(500)
    b.play()
    count += b.get_num_draws()  

  print count / 1e2