import hashlib
import secrets

from Config import ConfigFile as cf
import System


def convertToUnicode(string):
	result = []
	for letter in string:
		result.append(ord(letter))
	return result


def encryptionXOR(number, key):
	# Due to the fact that the ZIP function cuts off the resulting list
	# if two incoming list of different lengths are long, and we do not need this,
	# we write their implementation.
	# В связи с тем, что функция zip обрезает результирующий список,
	# если два входящих списка разной длинны, а нам такого не надо,
	# то пишем свою реализацию.

	# This code block defines which of the incoming lists is longer, and writes in and the longest.
	# This check is necessary to simplify the XOR block.
	# Данный блок кода определяет какой из входящих списков длиннее, и записывает в А самый длинный.
	# Это проверка необходима для упрощения блока XOR
	A = []
	B = []
	if len(number) > len(key) or len(number) == len(key):
		A = number
		B = key
	else:
		A = key
		B = number

	# Block XOR. With an XOR operation, elements from the B list can end, if the length A and B are different.
	# Therefore, zucing the brute force of the list of the list in, until the list is over.
	# That is, with Len (a) <Len (b), the list will be repeatedly applied.
	# Блок XOR. При операции XOR, элементы из списка В, могут закончится, если длина А и В, различны.
	# Поэтому зацикливаем перебор элементов списка В, до тех пор, пока список А не закончится.
	# То есть, при len(A) < len(B), список В будет многократно применятся.
	result = []
	indexB = 0
	for elementA in A:
		if indexB > len(B) - 1:
			indexB = 0
		result.append(elementA ^ B[indexB])
		indexB += 1

	return result


def createLUKstring(lenString):
	string = ""
	s = secrets.SystemRandom()
	for _ in range(lenString):
		string += str(chr(s.randint(33, 126)))
		# Symbol separator
		# Символ разделитель
		string += " "
	return string


def createLUK(lenLUK):
	# TODO #XX: Вынесці ў асобны метад config.get_full_luk_path()
	name_file = "LUK"
	path = cf.get_value_by_key("path_LUK")
	with open(f"{path}/{name_file}", 'w', encoding="utf-8") as f:
		f.write(createLUKstring(lenLUK))


def isLUKfile():
	return System.is_file("LUK", cf.get_value_by_key("path_LUK"))


def getHashString(string):
	hashObject = hashlib.sha256(bytes(string, 'utf-8'))
	return hashObject.hexdigest()


def getHashLUK():
	# Get a hash string from the file
	# Получаем хеш строки из файла
	# TODO #XX: Вынесці ў асобны метад config.get_full_luk_path()
	name_file = "LUK"
	path = cf.get_value_by_key("path_LUK")
	with open(f"{path}/{name_file}", 'r', encoding="utf-8") as f:
		return getHashString(f.read())


def convertToString(listUnicode):
	string = ""
	step = 8
	for elementList in listUnicode:
		# With an XOR operation, symbols outside 33 and 127 may appear.
		# To avoid this, we make two cycles with autocorrect number
		# При операции XOR, могут появляться символы за пределами 33 и 127.
		# Чтобы это избежать, делаем два цикла с автокоррекцией числа
		while elementList < 33:
			elementList += step
		while elementList > 127:
			elementList -= step

		string += chr(elementList)
	return string
