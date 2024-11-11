requests=[]
cache=[]

while True:
    first=input("What page would you like to request?")
    if first.upper()=="Q":
        break
    else:
        requests.append(int(first))

    while True:
        page_request=int(input("What page would you like to request?"))

        requests.append(page_request)              

        if page_request==0:            
            for i in requests:
                if i not in cache and i!=0:
                    if len(cache)<8:
                        cache.append(i)
                    else:
                        cache.pop(0)
                        cache.append(i)
                    print("miss")
                elif i in cache:
                    print("hit")

                
            print(cache)
            requests=[]
            cache=[]
            break
        