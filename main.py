# Author : Uday Indoria


from sm4 import *
import os, os.path
from datetime import datetime
#import time
class Experiment_P_C_RK():
    def __init__(self):
        print("Enter which round you want to capture [1-32]:")
        num_round = int(input())
        if num_round<1 or num_round>32:
            print("Invalid round...")
            return -1
        #no_of_encryptions = 0
        #encryption_time = 0.0
        print("\033[1;32mEncryption Started\033[0m")
        current_datetime = datetime.now()
        current_date_time = current_datetime.strftime("%d_%m_%Y-%H_%M_%S")
        data_file = open("dataset-"+current_date_time+".csv","w")
        data_file.write("Mainkey,CipherText,PlainText,RoundKey,ct_0,ct_1,ct_2,ct_3,ct_4,ct_5,ct_6,ct_7,ct_8,ct_9,ct_10,ct_11,ct_12,ct_13,ct_14,ct_15,ct_16,ct_17,ct_18,ct_19,ct_20,ct_21,ct_22,ct_23,ct_24,ct_25,ct_26,ct_27,ct_28,ct_29,ct_30,ct_31,ct_32,ct_33,ct_34,ct_35,ct_36,ct_37,ct_38,ct_39,ct_40,ct_41,ct_42,ct_43,ct_44,ct_45,ct_46,ct_47,ct_48,ct_49,ct_50,ct_51,ct_52,ct_53,ct_54,ct_55,ct_56,ct_57,ct_58,ct_59,ct_60,ct_61,ct_62,ct_63,ct_64,ct_65,ct_66,ct_67,ct_68,ct_69,ct_70,ct_71,ct_72,ct_73,ct_74,ct_75,ct_76,ct_77,ct_78,ct_79,ct_80,ct_81,ct_82,ct_83,ct_84,ct_85,ct_86,ct_87,ct_88,ct_89,ct_90,ct_91,ct_92,ct_93,ct_94,ct_95,ct_96,ct_97,ct_98,ct_99,ct_100,ct_101,ct_102,ct_103,ct_104,ct_105,ct_106,ct_107,ct_108,ct_109,ct_110,ct_111,ct_112,ct_113,ct_114,ct_115,ct_116,ct_117,ct_118,ct_119,ct_120,ct_121,ct_122,ct_123,ct_124,ct_125,ct_126,ct_127,pt_0,pt_1,pt_2,pt_3,pt_4,pt_5,pt_6,pt_7,pt_8,pt_9,pt_10,pt_11,pt_12,pt_13,pt_14,pt_15,pt_16,pt_17,pt_18,pt_19,pt_20,pt_21,pt_22,pt_23,pt_24,pt_25,pt_26,pt_27,pt_28,pt_29,pt_30,pt_31,pt_32,pt_33,pt_34,pt_35,pt_36,pt_37,pt_38,pt_39,pt_40,pt_41,pt_42,pt_43,pt_44,pt_45,pt_46,pt_47,pt_48,pt_49,pt_50,pt_51,pt_52,pt_53,pt_54,pt_55,pt_56,pt_57,pt_58,pt_59,pt_60,pt_61,pt_62,pt_63,pt_64,pt_65,pt_66,pt_67,pt_68,pt_69,pt_70,pt_71,pt_72,pt_73,pt_74,pt_75,pt_76,pt_77,pt_78,pt_79,pt_80,pt_81,pt_82,pt_83,pt_84,pt_85,pt_86,pt_87,pt_88,pt_89,pt_90,pt_91,pt_92,pt_93,pt_94,pt_95,pt_96,pt_97,pt_98,pt_99,pt_100,pt_101,pt_102,pt_103,pt_104,pt_105,pt_106,pt_107,pt_108,pt_109,pt_110,pt_111,pt_112,pt_113,pt_114,pt_115,pt_116,pt_117,pt_118,pt_119,pt_120,pt_121,pt_122,pt_123,pt_124,pt_125,pt_126,pt_127,rk_0,rk_1,rk_2,rk_3,rk_4,rk_5,rk_6,rk_7,rk_8,rk_9,rk_10,rk_11,rk_12,rk_13,rk_14,rk_15,rk_16,rk_17,rk_18,rk_19,rk_20,rk_21,rk_22,rk_23,rk_24,rk_25,rk_26,rk_27,rk_28,rk_29,rk_30,rk_31\n")
        path_keys = "key_files/"
        for key_files in [path_keys+f for f in os.listdir(path_keys) if os.path.isfile(os.path.join(path_keys,f))]:
            #print("\033[1;33mStarted\033[0m for Key File : "+key_files)
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
                    path_plaintext= "plaintext_files/"
                    for plaintext_files in [path_plaintext+f for f in os.listdir(path_plaintext) if os.path.isfile(os.path.join(path_plaintext,f))]:
                        #print("\033[1;36mStarted\033[0m for Plaintext File : "+plaintext_files)
                        with open(plaintext_files, "rb") as plaintext_file:
                            while(True):
                                plaintext = plaintext_file.read(16)
                                len_pt = len(plaintext)
                                if not len_pt:
                                    break
                                elif len_pt<16:
                                    zero=0
                                    plaintext += zero.to_bytes(16-len_pt, 'big')  
                                plaintext = int.from_bytes(plaintext, "big") 
                                #starttime = time.time()
                                ciphertext, roundkey = encrypt(plaintext, key, num_round)
                                #encryption_time += time.time()-starttime
                                #no_of_encryptions += 1
                                x=str(key)+","+str(ciphertext)+","+str(plaintext)+","+str(roundkey)
                                for i in range(128):
                                    x+=","+str(bin(ciphertext)[2:].zfill(128)[i])
                                for i in range(128):
                                    x+=","+str(bin(plaintext)[2:].zfill(128)[i])
                                for i in range(32):
                                    x+=","+str(bin(roundkey)[2:].zfill(32)[i])
                                x+="\n"
                                data_file.write(x)
                        #print("\033[1;32mFinished\033[0m for Plaintext File : "+plaintext_files)
            #print("\033[1;32mFinished\033[0m for Key File : "+key_files)
        data_file.close()
        print("\033[1;32mEncryption Finished\033[0m")
        #timefile = open("time.txt","w")
        #timefile.write("Total Encryptions made : "+str(no_of_encryptions)+"\nTotal Encryption Time : "+str(encryption_time)+" Seconds"+"\nAverage Encryption Time : "+str(encryption_time/no_of_encryptions)+" Seconds")
        #timefile.close()
if __name__ == '__main__':
    Experiment_P_C_RK()
