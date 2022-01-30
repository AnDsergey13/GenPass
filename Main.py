import GenPass as gp

# По умолчанию, используем вариант с интерфейсом. Если False, то работает в консольном режиме
UI = False

if UI:
	pass
else:
	
	privateKey = input("Введите приватный ключ: ")
	referenceWord = input("Введите слово-ориентир: ")

	encryptedPrivateKey = gp.getHashString(privateKey)
	encryptedPoluPublicKey = gp.getHashString(referenceWord)

	# Инверсируем элемнеты, так как при операции XOR, одинаковые числа не должны превращатся ноль.
	UnicodePrivateKey = gp.convertToUnicode(encryptedPrivateKey)[::-1]
	UnicodePoluPublicKey = gp.convertToUnicode(encryptedPoluPublicKey)

	A = gp.encryptionXOR(UnicodePoluPublicKey, UnicodePrivateKey)

	# При отсутствии файла LUK, генерируем количество символов и создаём его
	if not gp.isLUKfile():
		while True:
			# Чем больше указано количество символов, тем больше энтропия LUK ключа(наверное)
			numberLUKsymbols = input("Введите количество символов в LUK файле. Число должно быть больше 1000. По умолчанию задано число 5000: ")
			
			if numberLUKsymbols == "":
				numberLUKsymbols = 5000
				print(numberLUKsymbols)
				break
			try:
				if int(numberLUKsymbols) < 1001:
					print("*** Error. Слишком маленькое число. Число должно быть больше 1000")
					print("=================================================================")
				elif int(numberLUKsymbols) > 1000:
					break
			except:
				print("*** Error. Не верный ввод. Используйте только числа.")
				print("=================================================================")

		
	# 	gp.createLUK(numberLUKsymbols)
	
	# hashLUK = gp.getHashLUK(numberLUKsymbols)
	# B = gp.convertToUnicode(hashLUK)

	# result = gp.convertToString(gp.encryptionXOR(A, B))
	# print(result)