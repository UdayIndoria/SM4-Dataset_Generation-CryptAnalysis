from aes import AES
import os, os.path
class AES_GENERATE_FILES():
    def create_open_individual(self,path,filename,mode):
        files = list()
        for i in range(1,11):
            os.makedirs(os.path.dirname(path+str(i)+"RoundOutput/"+filename), exist_ok=True)
            files.append(open(path+str(i)+"RoundOutput/"+filename, mode))
        return files
    def create_open_combined(self,path,mode):
        files = list()
        for i in range(1,11):
            os.makedirs(os.path.dirname(path+str(i)+"RoundCombinedOutput"), exist_ok=True)
            files.append(open(path+str(i)+"RoundCombinedOutput", mode))
        return files
    def create_open_single_combined(self,path,mode):
        os.makedirs(os.path.dirname(path+"10RoundCombinedOutput"), exist_ok=True)
        return open(path+"10RoundCombinedOutput", mode)
    def __init__(self):
        print("\033[1;33mAES-128\tCTR MODE\tONLY COMBINED FILES\033[0m")
        print("\033[1;32mEncryption Started\033[0m")
        data_file = open("data.csv","w")
        data_file.write("Ciphertext File,Key,Plaintext File\n")
        path_ciphertext = "ciphertext_files/"
        cipher_file_no = 1
        #ciphertext_file_combined = self.create_open_combined(path_ciphertext,"wb")
        ciphertext_file_single_combined = self.create_open_single_combined(path_ciphertext,"wb")
        path_keys = "key_files/"
        for key_files in [path_keys+f for f in os.listdir(path_keys) if os.path.isfile(os.path.join(path_keys,f))]:
            print("\033[1;33mStarted\033[0m for Key File : "+key_files)
            with open(key_files, "rb") as key_file:
                while(True):
                    key = key_file.read(16)
                    len_key = len(key)
                    if not len_key:
                        break
                    elif len_key<16:
                        zero=0
                        key += zero.to_bytes(16-len_key, 'big') 
                    key = int.from_bytes(key, "big")
                    self.AES = AES(key)
                    #print("Key : "+str(hex(key)))
                    path_plaintext= "plaintext_files/"
                    for plaintext_files in [path_plaintext+f for f in os.listdir(path_plaintext) if os.path.isfile(os.path.join(path_plaintext,f))]:
                        #print("\033[1;36mStarted\033[0m for Plaintext File : "+plaintext_files)
                        counter = 0x00000000000000000000000000000000
                        with open(plaintext_files, "rb") as plaintext_file:
                            #ciphertext_file = self.create_open_individual(path_ciphertext,str(cipher_file_no),"wb")
                            data_file.write(str(cipher_file_no)+","+str(key)+","+plaintext_files.split("/")[-1]+"\n")
                            while(True):
                                plaintext = plaintext_file.read(16)
                                len_pt = len(plaintext)
                                if not len_pt:
                                    break
                                elif len_pt<16:
                                    zero=0
                                    plaintext += zero.to_bytes(16-len_pt, 'big') 
                                plaintext = int.from_bytes(plaintext, "big")
                                ciphertext = self.AES.encrypt(counter)
                                '''for i in range(0,10):
                                    #ciphertext_file[i].write(ciphertext[i].to_bytes(16, 'big'))
                                    ciphertext_file_combined[i].write(ciphertext[i].to_bytes(16, 'big'))'''
                                ciphertext_file_single_combined.write((ciphertext[-1] ^ plaintext).to_bytes(16, 'big'))
                                #print("Plaintext : "+str(hex(plaintext)))
                                #print("Ciphertext : "+str(hex(ciphertext)))
                                counter+=1
                            cipher_file_no+=1
                            '''for i in range(0,10):
                                ciphertext_file[i].close()'''  
                        #print("\033[1;32mFinished\033[0m for Plaintext File : "+plaintext_files)
            print("\033[1;32mFinished\033[0m for Key File : "+key_files)
        '''for i in range(0,10):
            ciphertext_file_combined[i].close()'''
        ciphertext_file_single_combined.close()
        data_file.close()
        print("\033[1;32mEncryption Finished\033[0m")
if __name__ == '__main__':
    AES_GENERATE_FILES()
