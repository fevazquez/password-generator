import string
import random
import sys

letters = string.ascii_letters
nums = string.digits
specials = string.punctuation

def getLength():
  length=12
  if len(sys.argv) > 1:
    requested = sys.argv[1]

    if requested.isnumeric():
      lenght = requested
    else:
      print(f'Requested lenght undefined. Please use an integer value. Using default size of {length}...')
    
  
  else:
    print(f'No password lenght provided on the command line. Using default size of {length}...')

  return length


def main():
    lexicon = letters + nums + specials
    length = getLength()
    password = ''.join(random.sample(lexicon, length))
    print('\n'+password+'\n')

    
if __name__ == '__main__':
    main()