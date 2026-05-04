import os
os.system('cls');

def sonAnagramas(p1, p2):
    p1 = p1.lower().replace(" ", "")
    p2 = p2.lower().replace(" ", "")
    
    if len(p1) != len(p2):
        return False
    
    return sorted(p1) == sorted(p2)

print(sonAnagramas('torpes', 'postre'))  # True
print(sonAnagramas('aparta', 'raptar'))  # False