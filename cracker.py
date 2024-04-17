import hashlib
import sys
def computeHashSHA256(salt, pword):
    salted = salt + pword
    return hashlib.sha3_256(salted).hexdigest()

def computeHashSHA512Digest(salt, pword):
    salted = pword + salt
    return hashlib.sha3_512(salted.encode("utf-8")).digest() 

def computeHashSHA512(salt, pword):
    salted = salt + pword
    return hashlib.sha3_512(salted).hexdigest()
#$6$NoDUcoDl3jyFo7oJ$a3kwknV522E3MVc2vyzWVgk2UHaB21v0//u2FZWfb/IAEcXghtz9Ad8YaEt0OAaKwNrdyLFJCdMNBiyfJEFHX.:19829:0:99999:7:::
def main():
    #print("SHA512: " + computeHashSHA512(b"NoDUcoDl3jyFo7oJ", b"zelda123"))
    b = computeHashSHA512Digest("NoDUcoDl3jyFo7oJ", "zelda123")
    with open('out.dat', 'wb') as f:
        f.write(b)

if __name__ == "__main__":
    main()