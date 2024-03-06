number=int(input("請輸入0~255的整數："))
if number>255 or number<0:
    print("超過範圍")
else:
    binary=[0]*8 #二進位
    hexa=[0]*2 #十六進位
    a=number #存取最一開始的number

    #十進位轉二進位
    for i in range(8):
        if number>=(2**(7-i)):
            binary[i]=1
            number=number-(2**(7-i))
        else:
            binary[i]=0
                
                #將二進位數字印出,從第一個不是0的數開始印
    print(a,"的二進位表示為：",end="")
    for i in range(8):
        if binary[i]!=0:
            break
    for j in range(i,8):
        print(binary[j],end="")
    print()

    #二進位轉十六進位
    hexa[0]=binary[0]*8+binary[1]*4+binary[2]*2+binary[3]
    hexa[1]=binary[4]*8+binary[5]*4+binary[6]*2+binary[7]
    for i in range(2):
        if hexa[i]==10:
            hexa[i]="A"
        if hexa[i]==11:
            hexa[i]="B"
        if hexa[i]==12:
            hexa[i]="C"
        if hexa[i]==13:
            hexa[i]="D"
        if hexa[i]==14:
            hexa[i]="E"
        if hexa[i]==15:
            hexa[i]="F"

    #將十六進位印出,從第一個不是0的數開始印
    print(a,"的十六進位表示為：",end="")
    for i in range(2):
        if hexa[i]!=0:
            break
    for i in range(i,2):
        print(hexa[i],end="")
        