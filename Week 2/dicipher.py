from Crypto.Cipher import AES
from Crypto.Util import Counter

def hex2char(hexstr) :
	charstr = ''
	for i in range(0,len(hexstr),2):
		charstr = charstr + chr(int(hexstr[i:i+2],16))
	return charstr

def decriptCBC(CBCKey,CBCCipher) :
	key        = hex2char(CBCKey)
	iv         = hex2char(CBCCipher[0:len(key)*2])
	ciphertext = hex2char(CBCCipher[len(key)*2:len(CBCCipher)])
	
	decryptAES = AES.new(key, AES.MODE_CBC, iv)
	
	text       = decryptAES.decrypt(ciphertext)
	return text

def decriptCTR(CTRKey,CTRCipher) :
	key        = hex2char(CTRKey)
	iv         = hex2char(CTRCipher[0:len(key)*2])
	ciphertext = hex2char(CTRCipher[len(key)*2:len(CTRCipher)])

	decryptAES = AES.new(key, AES.MODE_CTR, counter = Counter.new(128, initial_value=long(iv.encode("hex"), 16)))
	text = decryptAES.decrypt(ciphertext)
	return text

# Question 1
CBCKey    = '140b41b22a29beb4061bda66b6747e14'
CBCCipher = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
print decriptCBC(CBCKey,CBCCipher)

# Question 2
CBCKey    = '140b41b22a29beb4061bda66b6747e14'
CBCCipher = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253' 
print decriptCBC(CBCKey,CBCCipher)

# Question 3
CTRKey 	  = '36f18357be4dbd77f050515c73fcf9f2'
CTRCipher = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
print decriptCTR(CTRKey,CTRCipher)

# Question 4
CTRKey    = '36f18357be4dbd77f050515c73fcf9f2'
CTRCipher = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'
print decriptCTR(CTRKey,CTRCipher)
