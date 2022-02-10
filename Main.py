import GenPass as gp
# import UI

def processingNumLUK(number):
	# If you press Enter, the default values are set to 5000.
	# Если нажать Enter, то устанавливаются значения по умолчанию равным 5000.
	if number == "":
		number = 5000
		return int(number)

	try:
		if int(number) < 1001:
			# Input Error. Values should be less than 1000 
			# Ошибка ввода. Значения должны быть меньше 1000
			print(list_messages[4])
			print(list_messages[3])

			# The signal that the data entered did not pass conditions 
			# Сигнал о том, что вводимые данные не прошли условия
			return -1

		elif int(number) > 1000:
			return int(number)
	except:
		# Input Error. Symbols should not be used 
		# Ошибка ввода. Не должны использоваться символы
		print(list_messages[5])
		print(list_messages[3])

		# The signal that the data entered did not pass conditions 
		# Сигнал о том, что вводимые данные не прошли условия
		return -1

def getNumLUKsymbols():
	while True:
		# The greater the number of characters specified, the greater the entropy of the LUK-file
		# Чем больше указано количество символов, тем больше энтропия ЛУК-файла
		numberLUKsymbols = input(list_messages[2])
		
		numberLUKsymbols = processingNumLUK(numberLUKsymbols)
		if numberLUKsymbols != -1:
			return numberLUKsymbols

def getLanguageOS():
	import locale

	if locale.getdefaultlocale()[0] == "ru_RU":
		return "ru_RU"
	else:
		return "en_US"

def getMessages():
	messages = []
	with open(f"locale/{getLanguageOS()}",'r') as f:
		for line in f.readlines():
			# [:-1] Cut a new line symbol. He's not needed 
			# [:-1] Отрезаем символ новой строки. Он не нужен
			messages.append(line[:-1])

	return messages

# If True is used by the interface option. If False, it works in console mode
# Если True - используется вариант с интерфейсом. Если False, то работает в консольном режиме
USE_USER_INTERFACE = False

list_messages = getMessages()

if USE_USER_INTERFACE:
	pass
	# ui = UI.UIGP()
	# ui.createWindow()
else:
	privateKey = input(list_messages[0])
	landmarkPhrase = input(list_messages[1])

	encryptedPrivateKey = gp.getHashString(privateKey)
	encryptedLandmarkPhrase = gp.getHashString(landmarkPhrase)

	# Invert the elements, since during the XOR operation, the same keys should not turn zero. And when the keys were swapped, the same password was not created.
	# Инверсируем элемнеты, так как при операции XOR, одинаковые ключи не должны превращатся ноль. И при перестановке ключей местами, не создавался одинаковый пароль.
	UnicodePrivateKey = gp.convertToUnicode(encryptedPrivateKey)[::-1]
	UnicodeLandmarkPhrase = gp.convertToUnicode(encryptedLandmarkPhrase)

	A = gp.encryptionXOR(UnicodeLandmarkPhrase, UnicodePrivateKey)

	# In the absence of a LUK-file, we generate the number of characters and create it
	# При отсутствии ЛУК-файла, генерируем количество символов и создаём его
	if not gp.isLUKfile():
		numberLUKsymbols = getNumLUKsymbols()
		gp.createLUK(numberLUKsymbols)
	
	# If you do not change the hash to all capital letters, then the final password will be without capital letters (why?). Which reduces the complexity of the password itself.
	# Если не изменять Хэш на все заглавные буквы, то конечный пароль будет без заглавных букв (почему?). Что уменьшает сложность самого пароля. 
	hashLUK = gp.getHashLUK().upper()

	B = gp.convertToUnicode(hashLUK)

	result = gp.convertToString(gp.encryptionXOR(A, B))
	print(result)