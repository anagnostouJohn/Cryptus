from Crypto.Cipher import AES
import hashlib
import os
import pathlib

def encrypt_file(key,filein,fileout=None,IV=None):
    modes = [1,2,8,3,6,9,11,12,10,5]
    if os.path.isfile(filein):
        if IV == None:
            IV = 16 * b'\x00'
        else:
            IV = IV.encode("utf-8")
        if len(IV)==16:
            if fileout == None:
                fileout_path = pathlib.Path(filein).parent
                fileout_name = pathlib.Path(filein).name
            else:
                fileout_path = pathlib.Path(fileout).parent
                fileout_name = pathlib.Path(fileout).name
                print (fileout_path, fileout_name )
                if os.path.exists(fileout_path) == False:
                    print("Path Does Not Exists")
                    return

            encryptor = AES.new(hashlib.sha256(key.encode("utf-8")).digest(), 3, IV=IV)
            with open(filein,"rb") as f :
                f = f.read()
                encr_bytes = encryptor.encrypt(f)
                file = open(str(fileout_path)+"\\"+str(fileout_name)+".enc","wb")
                file.write(encr_bytes)
                file.close()
                del encryptor
        else:
            print ("IV must 16 bytes long")
            return
    else:
        print("No file path")
        return




def dencrypt_file(key,filein,fileout=None,IV=None,TXT = False):
    if os.path.isfile(filein):
        if IV == None:
            IV = 16 * b'\x00'
        else:
            IV = IV.encode("utf-8")
        if len(IV)==16:
            if fileout == None:
                fileout_path = pathlib.Path(filein).parent
                fileout_name = pathlib.Path(filein).name
                list_name = fileout_name.split(".")
            else:
                fileout_path = pathlib.Path(fileout).parent
                fileout_name = pathlib.Path(fileout).name
                list_name =  fileout_name.split(".")
                if os.path.exists(fileout_path) == False:
                    print("Path Does Not Exists")
                    return
            file_name = list_name[0] + "." + list_name[1]
            if os.path.isfile(str(fileout_path)+"\\"+str(file_name)):
                file_name = list_name[0] + "new" +"." + list_name[1]
                print(file_name, "OK")
            else:
                file_name = file_name
            final_path = str(fileout_path) + "\\" +  file_name
            encryptor = AES.new(hashlib.sha256(key.encode("utf-8")).digest(), 3, IV=IV)
            with open(filein,"rb") as f :
                if TXT == False:
                    file = open(final_path,"wb")
                    file.write(encryptor.decrypt(f.read()))
                    file.close()
                else:
                    return encryptor.decrypt(f.read()).decode("utf-8")
        else:
            print ("IV must 16 bytes long")
            return
    else:
        print("No file path")
        return









# print(AES.MODE_SIV)
# print(dir(AES))
#
# #dencrypt_file("sss","C:\\Users\\john\\Desktop\\MISP.txt.enc",IV="dededebfbfbfbfbf")
# x = dencrypt_file("sss","C:\\Users\\john\\Desktop\\MISP1.txt.enc","C:\\Users\\john\\Desktop\\MISP.txt",IV="dededebfbfbfbfbf",TXT=True)
# print(x)
# #encrypt_file("sss","C:\\Users\\john\\De33sktop\\MIddSP", IV="dededebfbfbfbfbf")
# #encrypt_file("sss","C:\\Users\\john\\Desktop\\MISP1.txt", IV="dededebfbfbfbfbf")