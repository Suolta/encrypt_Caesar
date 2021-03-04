print ("Script to encrypt the way Caesar..!?")
def test(txt,key):
  test_list = []
  for l in txt:
    position = ord(l)  #ord ""

    new_letter = chr(position + key) #ord(l) + key 

    test_list.append(new_letter)

  t  = ''.join(test_list)
  print(t)


text = list(input("Enter the your text: "))
key = int(input("Enter the your kay: "))
test(text,key)


