import hashlib
import secrets

from config import get_value_by_key
import system


def convert_to_unicode(string):
	result = []
	for letter in string:
		result.append(ord(letter))
	return result


def encryption_xor(number, key):
	# Due to the fact that the ZIP function cuts off the resulting list if two incoming list of different lengths are long, and we do not need this, we write their implementation.
	# В связи с тем, что функция zip обрезает результирующий список, если два входящих списка разной длинны, а нам такого не надо, то пишем свою реализацию.

	# This code block defines which of the incoming lists is longer, and writes in and the longest. This check is necessary to simplify the XOR block.
	# Данный блок кода определяет какой из входящих списков длиннее, и записывает в А самый длинный. Это проверка необходима для упрощения блока XOR
	# FIXME: Для чего эти инициализации пустыми списками?
	a = []
	b = []
	if len(number) > len(key) or len(number) == len(key):
		a = number
		b = key
	else:
		a = key
		b = number

	# Block XOR. With an XOR operation, elements from the B list can end, if the length A and B are different. Therefore, zucing the brute force of the list of the list in, until the list is over. That is, with Len (a) <Len (b), the list will be repeatedly applied.
	# Блок XOR. При операции XOR, элементы из списка В, могут закончится, если длина А и В, различны. Поэтому зацикливаем перебор элементов списка В, до тех пор, пока список А не закончится. То есть, при len(A) < len(B), список В будет многократно применятся.
	result = []
	index_b = 0
	for element_a in a:
		if index_b > len(b) - 1:
			index_b = 0
		result.append(element_a ^ b[index_b])
		index_b += 1

	return result


def create_luk_string(string_len):
	string = ""
	# TODO: переименовать переменную s
	s = secrets.SystemRandom()
	for _ in range(string_len):
		string += str(chr(s.randint(33, 126)))
		# Symbol separator
		# Символ разделитель
		string += " "
	return string


def create_luk(luk_len):
	# TODO: Вынести в отдельный метод config.get_full_luk_path()
	name_file = "LUK"
	path = get_value_by_key("path_LUK")
	with open(f"{path}/{name_file}", 'w', encoding="utf-8") as f:
		f.write(create_luk_string(luk_len))


def is_luk_file():
	# TODO: Вынести в отдельный метод config.get_full_luk_path()
	return system.is_file("LUK", get_value_by_key("path_LUK"))


def get_hash_string(string):
	hash_object = hashlib.sha256(bytes(string, 'utf-8'))
	return hash_object.hexdigest()


def get_hash_luk():
	# Get a hash string from the file
	# Получаем хеш строки из файла
	# TODO: Вынести в отдельный метод config.get_full_luk_path()
	name_file = "LUK"
	path = get_value_by_key("path_LUK")
	with open(f"{path}/{name_file}", 'r', encoding="utf-8") as f:
		return get_hash_string(f.read())


def convert_to_string(unicode_list):
	string = ""
	step = 8
	for elementList in unicode_list:
		# With an XOR operation, symbols outside 33 and 127 may appear. To avoid this, we make two cycles with autocorrect number
		# При операции XOR, могут появляться символы за пределами 33 и 127. Чтобы это избежать, делаем два цикла с автокоррекцией числа
		while elementList < 33:
			elementList += step
		while elementList > 127:
			elementList -= step

		string += chr(elementList)
	return string
