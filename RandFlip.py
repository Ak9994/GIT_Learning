import random
def Toss():
    flip = random.random()
    if(flip >= .5):
        return True
    else:
        return False

def flip(trial):
    heads = 0
    tails = 0
    result_count = " "

    for i in range(int(trial)):
        if ( Toss() ):
            heads += 1
            result_count += "H"
        else:
            tails += 1
            result_count += "T"
    
    print (result_count)
    print(heads)
    print(tails)            

trial = input(" input no of flips: ")
flip(trial)


                

