a={"kishore":"kishore123","rakkesh":"rak123","dharshan":"dha123","pyhon":"1234","pyy":"7"}
def main():
    
    user=input("if enter 2 new user and pass create or enter 1 already created:")
    if user == "1":
        login()
    if user  == "2":
        newuser()
        

    


def login():
    
    for i in a:
        b=input("enter a username:")
        if b in a:
            print("valid user name")
            c=input("enter a password:")
            if c == a[b]:
                print("valid pass")
                break
            else:
                print("wrong pass")
            for j in range(4):
                c=input("enter a password:")
                print(c)
                if c == a[b]:
                    print("crt pass")
                    break
                else:
                    print("wrong pass")
        else:
            print("wrong user name")

def newuser():
    newuse=input("enter a new username:")
    passs=input("enter a new password:")
    a[newuse]=passs
    print(a)
    if newuse in a:
        print("already created username")
    if passs in a[newuse]:
        print("already created password")
    
    


main()











          
       
    