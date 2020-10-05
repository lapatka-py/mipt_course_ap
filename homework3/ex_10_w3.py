class WrongValueException(Exception):
   pass


try:
   value = int(input("input positive number: "))
   if value < 0:
       raise WrongValueException("Wrong value: " + str(value))
   print(value + 10)
except WrongValueException as e:
  print(e)
