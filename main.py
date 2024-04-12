#### PYTHON BINARYGEN #### 




basenum = 22
inputnum = int(input("Enter A Number: "))


def binarygen(num):
  print(num % 2, end = "")
  if num > 0:
    binarygen(num // 2)

binarygen(basenum)




####END_CODE_MUCH_GOOD#### 