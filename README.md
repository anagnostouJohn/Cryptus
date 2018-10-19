# Cryptus
A simple programm that Envrypts - Decrypts individual files. 

<h3>Usage</h3>
<h2>Encrypt</h2></br>
encrypt_file(key,filein,fileout=None,IV=None) </br>

key : Secret key to encrypt a file</br>
filein : The file to be encrypted</br>
fileout : path to store the encrypted file (if not given the file will be stored alongside to unencrypted file)</br>
IV : The Initialization Vector (16 * b"\x00" if not given) </br>

<h2>Dencrypt</h2></br>
dencrypt_file(key,filein,fileout=None,IV=None,TXT = False)</br>
key : The secret key</br>
filein : The file to be unencrypted</br>
fileout : path to store the encrypted file (if not given the file will be stored alongside to decrypted file)</br>
IV : The Initialization Vector (16 * b"\x00" if not given) </br>
TXT : if TXT is returns the file as unencrypted string  (False by default)</br>
