abc = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XC':90,'XL':40,'CD':400,'CM':900}
def to_roman(num):
    roman = 0
    n = len(num)
    for i, j in enumerate(num):
        if i < n-1 and abc[j] < abc[num[i+1]]:
           roman = roman - abc[j]
        else:
            roman = roman + abc[j]

    return roman
print(to_roman(input()))