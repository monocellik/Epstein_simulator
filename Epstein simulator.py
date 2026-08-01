
print(
"""
--------------------------------------------------
EPSTIEN SIMULATOR
--------------------------------------------------

EEEE   PPPPP   SSSS   TTTTT   I   EEEE   N      N
E      P   P  S         T     I   E      NN     N
EEEE   PPPPP   SSSS     T     I   EEEE   N N    N
E      P          S     T     I   E      N  N   N
EEEE   P       SSSS     T     I   EEEE   N   N  N

SSSS   I   M     M
S      I   M M M M
SSSS   I   M  M  M  ....
   S   I   M     M  ....
SSSS   I   M     M  ....

--------------------------------------------------    
EPSTIEN SIMULATOR
--------------------------------------------------
"""
)
cpi=1
p=0
pnedeed=10
pupdate=0
while True:
    user_input = input("hit enter to epstien some kids: ")
    
 
    if user_input == '':
        print()
        print('u epsteined a', cpi, 'kids!')
        p += 1
        print('total kids epstiened:', p)
        print()
        
        if p > pnedeed:
            print(
            """
------------
U EPSTEINED A NIGGA!!!!
------------
            """
            )
            pnedeed = (pnedeed / 2) + (pnedeed * 2)
            cpi += 1
            
            print('epsteining effiency:', cpi)
            print('to next nigga kids nedeed:', pnedeed)
