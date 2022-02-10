import os
import hashlib
import secrets

def convertToUnicode(string):
	result = []
	for letter in string:
		result.append(ord(letter))
	return result

def encryptionXOR(number, key):
	# В связи с тем, что функция zip обрезает результиующий список, если два входящих списка разной длинны, а нам такого не надо, то пишем свою реализацию.

	# Данный блок кода определяет какой из входящих списков длинее, и записывает в А самый длинный. Это проверка необходима для упрощения блока ксора
	A = []
	B = []
	if len(number) > len(key) or len(number) == len(key):
		A = number
		B = key
	else:
		A = key
		B = number

	# Блок ксора. При операции ксор, элементы из списка В, могут закончится, если длина А и В, различны. Поэтому зацикливаем перебор элементов списка В, до тех пор, пока список А не закончится. То есть, при len(A) < len(B), список В будет многократно применятся.
	result = []
	indexB = 0
	for elementA in A:
		if indexB > len(B) - 1:
			indexB = 0
		result.append(elementA^B[indexB])
		indexB += 1

	return result

def createLUKstring(lenString):
	string = ""
	s = secrets.SystemRandom()
	for _ in range(lenString):
		string += str(chr(s.randint(33, 126)))
		# символ разделитель
		string += " "
	return string

def createLUK(lenLUK):
	with open("LUK",'w') as f:  
		f.write(createLUKstring(lenLUK))

def getHashString(string):
	hashObject = hashlib.sha256(bytes(string, 'utf-8'))
	return hashObject.hexdigest()

def isLUKfile():
	return os.path.exists("LUK")

def getHashLUK():
	# Получаем хэш строки из файла
	with open("LUK",'r') as f:  
		return getHashString(f.read())

def convertToString(listUnicode):
	string = ""
	step = 8
	for elementList in listUnicode:
		# при операции ксор, могут появлятся символы за пределами 33 и 127. Чтобы это избежать, делаем два цикла с автокоррекцией числа
		while elementList < 33:	elementList += step
		while elementList > 127: elementList -= step

		string += chr(elementList)
	return string
