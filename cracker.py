import crypt

def cracker(shadow, passwds):
    shadwFile = open(shadow, "r")
    for x in shadwFile:
        temp1 = x.split(":") #needs less confusing variable name
        uName = temp1[0]
        if(temp1[1] == "*"):
            pass
        else:
            temp2 = temp1[1].split('$') #same as temp1. can't think of anything at the moment
            salt = '$' + temp2[1] + '$' + temp2[2] + '$' #have to add these back in
            passwordFile = open(passwds, "r")
            for y in passwordFile:
                pwd = crypt.crypt(y.strip(), salt)
                if pwd == temp1[1]:
                    print("Username: " + uName)
                    print("Password: " + y.strip())
                    break
                else:
                    pass #this else statement is probably redundant
            passwordFile.close()
    shadwFile.close()
            

def main():
    cracker("shadow.txt", "passwords.txt")

if __name__ == "__main__":
    main()