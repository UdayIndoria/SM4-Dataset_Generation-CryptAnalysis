SM4 Encryption

Capturing the ciphertext after each rounds.

Instructions to use:
1. Place keys(files that contains keys) in the key_files folder.
2. Place plaintext (that has to be encrypted with the different keys) in the plaintext_files.
3. start terminal or command prompt (make sure working directory is same as the directory that contains codes and files).
4. run below command in terminal
4.1 For ECB MODE Without NONCE
python3 main_SM4_ECB_MODE_WO_NONCE.py
4.2 For ECB MODE With NONCE
python3 main_SM4_ECB_MODE_NONCE.py
4.3 For CBC MODE
python3 main_SM4_CBC_MODE.py
4.4 For CTR MODE 
python3 main_SM4_CTR_MODE.py
5. After successfull execution of the program, you will get the outputs.
6. data.csv file contains the data related to the ciphertext file, plaintext file name of particular ciphertext file, and the key in which plaintext encrypted.
7.1. Inside ciphertext_files directory you will get the 32 ciphertext files (each file is output of different rounds; and these files are combined form of all the ciphertext generated from plaintext with different keys).
7.2. Inside ciphertext_files directory you will get the 32 directories (each directory is output of different roubds) in which several ciphertext files are stored. Every file is encrypted file of the plaintext with different keys. [Individual Files Generation Codes Are Commented, You Need To Uncomment It If You Want To Get Individual Files.]



NOTE:
1. This program will overwrite existing ciphertext files and data.csv file, so please move to another directory or rename it.
2. No need to configure anything.
3. No need to give input file names for key and plaintext, It will automatically get all the key files and plaintext files from the respective directories.
4. Just run the code with the sample files already given. and see the ** MAGIC **
