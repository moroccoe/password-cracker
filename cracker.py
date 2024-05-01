import crypt

def cracker(shadow, passwds):
    shadowFile = open(shadow, "r")
    passwordFile = open(passwds, "r") 
    passwordList = []
    for y in passwordFile:
        passwordList.append(y.strip())
    passwordFile.close()
    for x in shadowFile:
        loginComponents = x.split(":") 
        uName = loginComponents[0]
        if(loginComponents[1] != "*"):
            hashComponents = loginComponents[1].split('$') 
            hashId = hashComponents[1]
            salt = '$' + hashId + '$' + hashComponents[2] + '$' 
            for y in passwordList:
                pwd = crypt.crypt(y, salt)
                if pwd == loginComponents[1]:
                    print("Username: " + uName)
                    print("Password: " + y.strip())
                    break
            
    shadowFile.close()
            

def main():
    print("Enter shadowfile name: ")
    shadow = str(input())
    print("Enter password dictionary file name: ")
    password = str(input())
    cracker(shadow, password)

if __name__ == "__main__":
    main()