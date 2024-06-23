
#Swaping lower to upper vice versa
def swap_case(s):
  string = ''.join(char.swapcase() for char in s)
  return string


if __name__ == '__main__':
    s = input()
    swap_case(s)
    print(s)