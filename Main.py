import GenPass as gp
import UI

import sysconfig

def processingNumLUK(number):
	# Если нажать Enter, то устанавливаются значения по умолчанию равным 5000.
	if number == "":
		number = 5000
		return int(number)

	try:
		if int(number) < 1001:
			print(list_messages[2])
			print(list_messages[1])
			# Сигнал о том, что вводимые данные не прошли условия
			return -1
		elif int(number) > 1000:
			return int(number)
	except:
		print(list_messages[3])
		print(list_messages[1])
		# Сигнал о том, что вводимые данные не прошли условия
		return -1


def getNumLUKsymbols():
	while True:
		# Чем больше указано количество символов, тем больше энтропия LUK ключа(наверное)
		numberLUKsymbols = input(list_messages[0])
		
		numberLUKsymbols = processingNumLUK(numberLUKsymbols)
		if numberLUKsymbols != -1:
			return numberLUKsymbols


list_messages = ["Введите количество символов в LUK файле. Число должно быть больше 1000. По умолчанию задано число 5000: ",
				"\n=================================================================",
				"*** Error. Слишком маленькое число. Число должно быть больше 1000",
				"*** Error. Не верный ввод. Используйте только числа."]

# Тип ОС
TYPE_OS = [
	[0, "Arch"],
	[1, "Android"],
	[2, "Windows"]
]

# По умолчанию Arch Linux
CURRENT_OS = TYPE_OS[0]

if sysconfig.get_platform() == "linux-x86_64": 
	CURRENT_OS = TYPE_OS[0]
elif sysconfig.get_platform() == "linux-aarch64": 
	CURRENT_OS = TYPE_OS[1]


# По умолчанию True - используется вариант с интерфейсом. Если False, то работает в консольном режиме
useUserInterface = True



if useUserInterface:
	ui = UI.UIGP(CURRENT_OS)
	ui.createWindow()
else:
	privateKey = input("Введите приватный ключ: ")
	referenceWord = input("Введите слово-ориентир: ")

	encryptedPrivateKey = gp.getHashString(privateKey)
	encryptedPoluPublicKey = gp.getHashString(referenceWord)

	# Инверсируем элемнеты, так как при операции XOR, одинаковые числа не должны превращатся ноль.
	UnicodePrivateKey = gp.convertToUnicode(encryptedPrivateKey)#[::-1]
	UnicodePoluPublicKey = gp.convertToUnicode(encryptedPoluPublicKey)

	A = gp.encryptionXOR(UnicodePoluPublicKey, UnicodePrivateKey)

	# При отсутствии файла LUK, генерируем количество символов и создаём его
	if not gp.isLUKfile():
		numberLUKsymbols = getNumLUKsymbols()
		gp.createLUK(numberLUKsymbols)
	
	# Если не изменять Хэш на все заглавные буквы, то конечный пароль будет без заглавных букв (из-за особенностей XOR). Что уменьшает сложность самого пароля. 
	hashLUK = gp.getHashLUK().upper()

	B = gp.convertToUnicode(hashLUK)

	result = gp.convertToString(gp.encryptionXOR(A, B))
	print(result)