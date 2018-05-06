# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_func(s, prime, multiplier):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans

def precomputeHash(text, pattern, prime, multiplier):
    TminusP = len(text)-len(pattern)
    H = [0]*(TminusP+1)
    lastFrame = text[TminusP:]
    H[TminusP] = hash_func(lastFrame, prime, multiplier)
    
    y=1
    for i in range(1,len(pattern)+1):
        y = (y*multiplier) % prime
    i=TminusP-1
    while i>=0:
        H[i] = (multiplier*H[i+1] + ord(text[i]) - y*ord(text[i+len(pattern)]) )% prime
        i-=1
    return H

def get_occurrences(pattern, text):
    prime = 1000000007
    multiplier = 263
    result = []
    patternHash = hash_func(pattern, prime, multiplier)
    H = precomputeHash(text, pattern, prime, multiplier)
    for i in range(len(text)-len(pattern)+1):
        if patternHash != H[i]: continue
        if text[i:i+len(pattern)] == pattern : result.append(i)
    return result
    '''    
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]'''

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

