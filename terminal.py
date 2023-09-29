import gen_pass as gp
from localization import get_text as _


def processingNumLUK(number):
	# If you press Enter, the default values are set to 5000.
	# Если нажать Enter, то устанавливаются значения по умолчанию равным 5000.
	if number == "":
		number = 5000
		return int(number)

	try:
		if int(number) < 1001:
			# Input Error. The values must be greater than 1000
			# Ошибка ввода. Значения должны быть больше 1000
			print(_("Err. LUK-file. Greater than 1000"))
			# print(localization[3]) - выдаліць?

			# The signal that the data entered did not pass conditions
			# Сигнал о том, что вводимые данные не прошли условия
			return -1

		elif int(number) > 1000 and int(number) < 1000000:
			return int(number)
		elif int(number) >= 1000000:
			# If the number is more than a million
			# Если число больше миллиона
			print(_("Err. LUK-file. Less than 1000000"))

			# The signal that the data entered did not pass conditions
			# Сигнал о том, что вводимые данные не прошли условия
			return -1

	except ValueError:
		# Input Error. Symbols should not be used
		# Ошибка ввода. Не должны использоваться символы
		print(_("Err. Invalid input"))

		# The signal that the data entered did not pass conditions
		# Сигнал о том, что вводимые данные не прошли условия
		return -1


def getNumLUKsymbols():
	while True:
		# The greater the number of characters specified, the greater the entropy of the LUK-file
		# Чем больше указано количество символов, тем больше энтропия ЛУК-файла
		luk_symbols_number = input(_("Enter. LUK-file. Default is 5000"))

		luk_symbols_number = processingNumLUK(luk_symbols_number)
		if luk_symbols_number != -1:
			return luk_symbols_number


def Main():
	private_key = input(_("Enter. Private key"))
	landmarkPhrase = input(_("Enter. Landmark phrase"))

	encryptedPrivateKey = gp.get_hash_string(private_key)
	encryptedLandmarkPhrase = gp.get_hash_string(landmarkPhrase)

	# Invert the elements, since during the XOR operation, the same keys should not turn into zero. And when the keys were swapped, the same password was not created.
	# Инвертируем элементы, так как при операции XOR, одинаковые ключи не должны превращаться в ноль. И при перестановке ключей местами, не создавался одинаковый пароль.
	UnicodePrivateKey = gp.convert_to_unicode(encryptedPrivateKey)[::-1]
	UnicodeLandmarkPhrase = gp.convert_to_unicode(encryptedLandmarkPhrase)

	A = gp.encryption_xor(UnicodeLandmarkPhrase, UnicodePrivateKey)

	# In the absence of a LUK-file, we generate the number of characters and create it
	# При отсутствии ЛУК-файла, генерируем количество символов и создаём его
	if not gp.is_luk_file():
		numberLUKsymbols = getNumLUKsymbols()
		gp.create_luk(numberLUKsymbols)

	# If you do not change the hash to all capital letters, then the final password will be without capital letters (why?). Which reduces the complexity of the password itself.
	# Если не изменять Хеш на все заглавные буквы, то конечный пароль будет без заглавных букв (почему?). Что уменьшает сложность самого пароля.
	hashLUK = gp.get_hash_luk().upper()

	B = gp.convert_to_unicode(hashLUK)

	result = gp.convert_to_string(gp.encryption_xor(A, B))
	print(result)
