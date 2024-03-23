c=1
def Hello(name):
    global c
    if c==11:
        return
    print(f'My Name Is {name}')

    c+=1
    Hello(name)



Hello(name='Hamza Ghaffar')
print(c)