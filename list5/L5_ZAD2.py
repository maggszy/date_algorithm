from helpy import Stack

def moveDisc(src_p,dest_p,extra_p):
    dest_p[1].push(src_p[1].pop())
    print("moving disc from",src_p[0],"to",dest_p[0])
    print(src_p[0],"=",src_p[1], extra_p[0],"=",extra_p[1], dest_p[0],"=",dest_p[1])

def moveTower(nDiscs,src_p,extra_p,dest_p):
    if nDiscs==0:
        return "Your Tower of Hanoi is empty!"
    elif nDiscs == 1:
        moveDisc(src_p, dest_p,extra_p)
    else:
        moveTower(nDiscs-1, src_p,dest_p, extra_p)
        moveDisc(src_p, dest_p,extra_p)
        moveTower(nDiscs-1, extra_p, src_p, dest_p)

def Hanoi(nDiscs,src,extra,dest):
    src_p= (src,Stack()) #(nazwa słupka,zawartość)
    extra_p=(extra,Stack())
    dest_p=(dest,Stack())
    
    for i in range(nDiscs):
        src_p[1].push(nDiscs-i)
        
    return moveTower(nDiscs,src_p,extra_p,dest_p)


if __name__ == "__main__":
    Hanoi(4,"A","B","C")