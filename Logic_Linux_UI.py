import Linux_UI as lui
import GenPass as gp

def Main(localization):
	ui = lui.UIGP(localization)
	ui.createWindow()

	# privateKey = ui.getPrivateKey()
	# landmarkPhrase = ui.getLandmarkPhrase()

	# encryptedPrivateKey = gp.getHashString(privateKey)
	# encryptedLandmarkPhrase = gp.getHashString(landmarkPhrase)

	# UnicodePrivateKey = gp.convertToUnicode(encryptedPrivateKey)[::-1]
	# UnicodeLandmarkPhrase = gp.convertToUnicode(encryptedLandmarkPhrase)

	# A = gp.encryptionXOR(UnicodeLandmarkPhrase, UnicodePrivateKey)

	# if not gp.isLUKfile():
	# 	numberLUKsymbols = getNumLUKsymbols()
	# 	gp.createLUK(numberLUKsymbols)

	# hashLUK = gp.getHashLUK().upper()

	# B = gp.convertToUnicode(hashLUK)

	# result = gp.convertToString(gp.encryptionXOR(A, B))
	# ui.setPassword(result)