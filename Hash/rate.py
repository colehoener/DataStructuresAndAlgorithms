import random
import open_hash

collisions = 0

print("   n |  Hash 1 (Avg Rate) | Hash 2 (Avg Rate) | Hash 3 (Avg Rate)  ")

for n in range(1, 12):
    #Hash 1
    H=open_hash.OpenHash(5,open_hash.hash1)
    for i in range(0, n):
        H.insert(random.randint(0, 5*n))

    for j in range(0, len(H.data)):
        if(len(H.data[j]) > 1):
            collisions+=1
    
    hoc = collisions / n

    #reset
    collisions = 0

    #Hash 2
    H=open_hash.OpenHash(5,open_hash.hash2)
    for i in range(0, n):
        H.insert(random.randint(0, 5*n))

    for j in range(0, len(H.data)):
        if(len(H.data[j]) > 1):
            collisions+=1
    
    htc = collisions / n

    #reset
    collisions = 0

    #Hash 3
    H=open_hash.OpenHash(5,open_hash.hash3)
    for i in range(0, n):
        H.insert(random.randint(0, 5*n))

    for j in range(0, len(H.data)):
        if(len(H.data[j]) > 1):
            collisions+=1
    
    htrc = collisions / n

    print("%4d |  %11.3f       |  %11.3f      |  %11.3f"%(2**n, hoc, htc, htrc))
    

