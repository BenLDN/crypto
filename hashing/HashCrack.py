#this is a very serious and dangerous hacking script: if you give it an SHA-512 hash that was generated
#from a password of max 6 small characters of the English alphabet then it migh crack it within a reasonable amount of time
#you can generate SHA-512 hashes here: http://passwordsgenerator.net/sha512-hash-generator/

import hashlib
import itertools
import time

#defining the function that generates the SHA-512 hash of a string
def hash512(pw):    
    return hashlib.sha512(pw.encode('utf-8')).hexdigest().upper()

#iterating function from here: http://stackoverflow.com/questions/11747254/python-brute-force-algorithm
def bruteForce(charset, maxlength): 
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

#the actual cracking algorithm
def crack512(hashToCrack):

    #defining our char set - we're not using chars_cap yet but it might be useful later if I decide to take over the world
    chars_small='abcdefghijklmnopqrstuvwxyz'
    chars_cap=chars_small.upper()

    #pw not cracked just yet (haven't even started trying...)
    cracked=False

    #check all the possible combinations of strings up to 6 character
    for pwTry in bruteForce(chars_small,6):
        if hash512(pwTry)==hashToCrack:
            cracked=True
            break
    #if cracked, return the pw
    if cracked==True:
        return pwTry

    #otherwise accept defeat
    else:
        return "0"

def main():
    print("Insert the SHA 512 hash:")
    hashInput=input()

    #measuring the time spent on cracking
    start = time.time()

    pwCracked=crack512(hashInput.upper())
    end = time.time()

    if pwCracked!="0":
        print("Pw is: "+pwCracked)
        print("It took me "+str(end-start)+" seconds to crack it.")
    else:
        print("Pw not cracked this time. It must be very strong. Like numbers or something.")

if __name__=="__main__":
    main()
