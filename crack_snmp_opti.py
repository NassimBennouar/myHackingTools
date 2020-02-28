#!/usr/bin/python
import hashlib

final="3081800201033011020420dd06a7020300ffe30401050201030431302f041180001f8880e9bd0c1d12667a5100000000020105020120040475736572040cb92621f4a93d1bf9738cd5bd04003035041180001f8880e9bd0c1d12667a51000000000400a11e02046b4c5ac20201000201003010300e060a2b06010201041e0105010500"
msgAuthenticationParameters="b92621f4a93d1bf9738cd5bd"
blank=final.replace(msgAuthenticationParameters,"000000000000000000000000")
msgAuthoritativeEngineID="80001f8880e9bd0c1d12667a5100000000".decode('hex')

def calculerMD5(password):
	passwordlen =  len(password)
	if passwordlen == 0:
		return ""
	password_buf = ""
	count = 0
	password_index = 0
	while count < 1048576:
		for i in range(64):
			password_buf += password[password_index % passwordlen]
			password_index += 1
		count += 64
	h = hashlib.new('md5')
	h.update(password_buf)
	key = h.hexdigest().decode('hex')
	strpass = key + msgAuthoritativeEngineID + key
	h = hashlib.new('md5')
	h.update(strpass)
	key = h.hexdigest()
	entend_key = key + '00' * 48
	IPAD = '36' * 64
	k1 = "%0128x" % (int(entend_key, 16) ^ int(IPAD, 16))
	OPAD = '5c' * 64
	k2 = "%0128x" % (int(entend_key, 16) ^ int(OPAD, 16))
	input = k1 + blank
	h = hashlib.new('md5')
	h.update(input.decode('hex'))
	input = h.hexdigest()
	input = k2 + input
	h = hashlib.new('md5')
	h.update(input.decode('hex'))
	input = h.hexdigest()
	return input[:12*2]

with open('/home/chapavoler/hack/bruteforce/dico/rockyou.txt') as lol:
	i=0
	for l in lol:
		password = l[:-1]
		truc = calculerMD5(password)
		i += 1
		if i % 10000 == 0:
			print str(i)+" tries"
		if msgAuthenticationParameters == truc:
			print password
			break