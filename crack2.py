from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib, os, getpass, requests

TARGETS = ['Scott Farquhar', 'Lei Jun', 'Reid Hoffman', 'Zhou Qunfei', 'Jeff Bezos', 'Shiv Nadar', 'Simon Xie', 'Ma Huateng', 'Ralph Dommermuth', 'Barry Lam', 'Nathan Blecharczyk', 'Judy Faulkner', 'William Ding', 'Scott Cook', 'Gordon Moore', 'Marc Benioff', 'Michael Dell', 'Yusaku Maezawa', 'Yuri Milner', 'Bobby Murphy', 'Larry Page', 'Henry Samueli', 'Jack Ma', 'Jen-Hsun Huang', 'Jay Y. Lee', 'Joseph Tsai', 'Dietmar Hopp', 'Henry Nicholas, III.', 'Dustin Moskovitz', 'Mike Cannon-Brookes', 'Robert Miller', 'Bill Gates', 'Garrett Camp', 'Lin Xiucheng', 'Gil Shwed', 'Sergey Brin', 'Rishi Shah', 'Denise Coates', 'Zhang Fan', 'Michael Moritz', 'Robin Li', 'Andreas von Bechtolsheim', 'Brian Acton', 'Sean Parker', 'John Doerr', 'David Cheriton', 'Brian Chesky', 'Wang Laisheng', 'Jan Koum', 'Jack Sheerack', 'Terry Gou', 'Adam Neumann', 'James Goodnight', 'Larry Ellison', 'Wang Laichun', 'Masayoshi Son', 'Min Kao', 'Hiroshi Mikitani', 'Lee Kun-Hee', 'David Sun', 'Mark Scheinberg', 'Yeung Kin-man', 'John Tu', 'Teddy Sagi', 'Frank Wang', 'Robert Pera', 'Eric Schmidt', 'Wang Xing', 'Evan Spiegel', 'Travis Kalanick', 'Steve Ballmer', 'Mark Zuckerberg', 'Jason Chang', 'Lam Wai Ying', 'Romesh T. Wadhwani', 'Liu Qiangdong', 'Jim Breyer', 'Zhang Zhidong', 'Pierre Omidyar', 'Elon Musk', 'David Filo', 'Joe Gebbia', 'Jiang Bin', 'Pan Zhengmin', 'Douglas Leone', 'Hasso Plattner', 'Paul Allen', 'Meg Whitman', 'Azim Premji', 'Fu Liquan', 'Jeff Rothschild', 'John Sall', 'Kim Jung-Ju', 'David Duffield', 'Gabe Newell', 'Scott Lin', 'Eduardo Saverin', 'Jeffrey Skoll', 'Thomas Siebel', 'Kwon Hyuk-Bin']
yes=["DCIM-0533.jpg.hacked","DCIM-0534.jpg.hacked","DCIM-0535.jpg.hacked","DCIM-0536.jpg.hacked"]
def xorbytes(a, b):
	len(a)
	if not len(a) == len(b):
		raise AssertionError
	res=bytearray([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
	for i in range(0,len(a)):
		res[i]=a[i] ^ b[i]

	return res

username="Jack Sheerack"
hsh = hashlib.new('md5')
hsh.update(username)
key = hsh.digest()
cip = AES.new(key, 1);
hohoho=""
for filename in yes:
	with open("vacation pictures/"+filename, 'rb') as (fi):
		with open(filename+"hoho.jpg", 'wb') as (fo):
			iv=bytearray(fi.read(16))
			aes2=fi.read(16)
			#print(iv);
			#print(len(iv));
			while aes2:
				#while len(aes2) < 16:
				#	aes2 += bytes([0])
				#aes2=fi.read(16);
				#print(aes2);
				xorShit=bytearray(cip.decrypt(aes2));
				#print(len(xorShit));
				content=xorbytes(iv,xorShit);
				#print(username)
				#wsh=""
				
				#for i in content :
				#	wsh+=hex(i)+" "
				#	hohoho+=chr(i);

				#print(wsh+"\n"+hohoho+"\n")
				#print(len(content));
				fo.write(content);
				iv=bytearray(aes2)
				aes2=fi.read(16)

	#print(hohoho)
#Jack Sheerack FFE0????4A464946000102??????????

#FFE000204A4649460001020000640064