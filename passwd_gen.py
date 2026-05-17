#MIT License
#
#Copyrigth (c) 2026 9arya
import random, string, base64
import sys
def main():
    p=0
    if len(sys.argv) < 2:
        p += 30
    elif (sys.argv[1]).lower() == "google":
        p += 100
    else:
        p += int(sys.argv[1])
    mo=""
    for n in range(p):
        d=random.choice(string.printable)
        mo+=mo.join(d)
    result="".join(mo)
    SecondResult = base64.z85encode(result.encode())
    LastResult=SecondResult.decode()
    print(LastResult[0:p])
if __name__=="__main__":
    main()
#this python script usefull for generate password
#how to use:
#python [NAME_SCRIPT_FILE] [PASSWORD_LENGTH]
#python [NAME_SCRIPT_FILE] [ACCOUNT_TYPE]
#for example:
#python passwd_gen.py 60
