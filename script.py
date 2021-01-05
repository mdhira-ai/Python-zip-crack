
# python version Python 3.9.1

import zipfile                  
import argparse                 #argparse version '1.1'
from threading import Thread    
import time


def extract_zip(zip_file, password):
    try:
        with open(password, 'r') as a:
            for i in a.readlines():
                passw = i.strip('\n')
                time.sleep(0.3)
                try:

                    with zipfile.ZipFile(zip_file) as myzipfile:
                        print(f'[-] password : { passw }')
                        a = myzipfile.extractall(pwd=passw.encode())
                        print(f'[+] password found : {passw} \n')

                    break

                except Exception as e:
                    pass

    except Exception as e:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-z', help='zip file path')
    parser.add_argument('-d', help='password list file path')
    args = parser.parse_args()

    zipname = args.z
    passname = args.d

    t = Thread(target=extract_zip, args=(zipname, passname))
    t.start()


if __name__ == "__main__":
    main()
