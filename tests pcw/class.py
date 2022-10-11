import random 
def almost_sorted(n):
    return [i + random.randint(0, 2) for i in range(n)]

# running this for a simple case
almost_sorted(5)