hook=[3,4,-2,-5]
hilt=[4,5,-5,-3]
pegLeg=[3,-2,2,-4]
hat=[3,2,-2,-3]
tyeDye=[-3,-3,2,4]
mitten=[-3,-3,1,5]
gloves=[-2,2,-2,-5]
beanie=[-3,0,-1,4]
#Product numbers: hook 1, hilt 2, peg leg 3, etc.
deals=[0,0,0,0]
winning=False
repChange=[0,0,0,0]
brian=50
stabby=61
pete=39
mittenbeard=50
reps=[brian,stabby,pete,mittenbeard]
products=[hook,hilt,pegLeg,hat,tyeDye,mitten,gloves,beanie]

def setChange(productOne,productTwo,productThree):
    for j in range(4):
        repChange[j]+=productOne[j]
        repChange[j]+=productTwo[j]
        repChange[j]+=productThree[j]
def win():
    print("victory or whatever")



for i in range(30):
    repChange=[0,0,0,0]
    first=int(input("input product number"))-1
    second=int(input("input product number"))-1
    third=int(input("input product number"))-1
    #Product numbers correspond to the order above
    setChange(products[first],products[second],products[third])
    print(repChange)
    for k in range(4):
        reps[k]+=repChange[k]
        if reps[k]>90:
            reps[k]=90
        elif reps[k]<10:
            reps[k]=10
        print(reps[k])
    print("day",i+1,"complete. Next day")

    for l in range(4):
        if reps[l]>=80:
            deals[l]=1
        elif reps[l]<=20:
            deals[l]=0
    if (deals[0]+deals[1]+deals[2]+deals[3])>=3:
        winning=True
    if i<=29:
        winning=False
if winning==True:
    win()
else:
    print("you suck you stupid idiot. I don't even comprehend how you could be so small brained.\nYour brain must be so incomprehensibly small and smooth that it defies logic. I truly do not know how someone with such a low functioning intellect can exist in this world.")