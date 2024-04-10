import hashlib

def computeHashSHA256(salt, pword):
    salted = salt + pword
    return hashlib.sha3_256(salted).hexdigest()

def computeHashSHA512(salt, pword):
    salted = salt + pword
    return hashlib.sha3_512(salted).hexdigest()

def main():
    print("SHA256: " + computeHashSHA256(b"87w74893749832749823", b"kali"))
    print("SHA512: " + computeHashSHA512(b"87w74893749832749823", b"kali"))
if __name__ == "__main__":
    main()