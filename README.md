# Cryptus
A simple programm that Envrypts - Decrypts individual files. 

<h3>Usage</h3>
<h2>Encrypt</h2>
encrypt_file(key,filein,fileout=None,IV=None)

key : Secret key to encrypt a file
filein : The file to be encrypted
fileout : path to store the encrypted file (if not given the file will be stored alongside to unencrypted file)
IV : The Initialization Vector (16 * b"\x00" if not given) 

<h2>Dencrypt</h2>
dencrypt_file(key,filein,fileout=None,IV=None,TXT = False)
key : The secret key
filein : The file to be unencrypted
fileout : path to store the encrypted file (if not given the file will be stored alongside to decrypted file)
IV : The Initialization Vector (16 * b"\x00" if not given) 
TXT : if TXT is returns the file as unencrypted string  (False by default)
