

for i in range(100):
    flag = False
    if i<=1:
        pass
        #print(f"Not Prime {i}")
    else:
        for j in range(2, i):
            if i% j==0:
                flag=True
                #print(f"NUmber {i} is prime.")
                break

        if flag:
            pass
            # print(f"Not Prime {i}")
        else:
            print(f"Prime {i}")