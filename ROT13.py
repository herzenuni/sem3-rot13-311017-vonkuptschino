#*********************FUNCTIONS******************************
import string

def ROT13(string):
  """
  DOCUMENTATION DOWN BELOW
  Функция для шифрования строки по алгоритму rot13.
  
  Аргумент функции 'string' - исходная строка
  
  return возвращает искомую строку 
  """

  def roter(ch):
    i = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(ch)
    if i != -1:
      return 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'[i]
    else:
      return ch

  return "".join(map(roter, string))
#ASSERTIONS  
if __name__ == "__main__":
	assert(ROT13(ROT13('pythonist wannabe')) == 'pythonist wannabe')  

#EXAMPLES  
#print('\n',ROT13('sbbone rttfcnz')) #foobar eggspam
#print('\n',ROT13('Hayrff rkcyvpvgyl fvyraprq')) #Unless explicitly silenced
#print('\n',ROT13('Gung jnl znl abg or boivbhf ng svefg hayrff lbh\'er Qhgpu'),'\n') #That way may not be obvious at first unless you're Dutch

def inputChekcer(userInput = " ", type = str):
	"""
	DOCUMENTATION DOWN BELOW
	Функция для проверки ввода через тип 
	"""
	while (1):
		try:
			inp = type(input(userInput))
			break
		except ValueError:
			print("\n\t\t\t\tInput error")
	return inp

def en_de_crypt_file():
	spase = "\n\n"
	try:
		filePath = inputChekcer("\tinput the path : ",str)
		justFile = open(filePath, "r")
		message = ROT13(justFile.read())
		justFile = open(filePath, "w")
		justFile.write(ROT13(message)) #исходное сообщение
		justFile.write(spase)
		justFile.write(message) #перекодированнoе сообщение
		print ('\n\t\t\tDecoding welldone!\n\n\n')
	except OSError:
		print("\tfailed opening the file for reading")
	finally: 
		justFile.close()
	
	
#***********************PROGRAMM*******************************

print("\t\t1) encrypt/decrypt file")
print("\t\t2) encrypt/decrypt string")
print("\t\t3) exit")

while(1):
	checker = input("\n\t\t\tinput: ")
	if checker == 1:
		en_de_crypt_file()
	elif checker == 2:
		print(ROT13(inputChekcer("\tInput the string: ",str)))
	elif checker == 3:
		exit()
	else:
		print("\tInput error. Repeat once again")
		 
