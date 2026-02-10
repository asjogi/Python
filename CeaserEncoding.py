
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# print(alpha.append('a'))

def convert(ltext,shift):
    word = ''
    for i in ltext:
        if i != ' ':
            num = alpha.index(i)
            encrypt = num + shift
            # print(f"'out: '{encrypt}")
            if encrypt > 25:
                encrypt = 25 - encrypt 
                # print(f"'inside if: '{abs(encrypt)}")
            word = word + alpha[abs(encrypt)]
        else: word = word + i
    return(word)
# print(word)


def reconvert(word,rshift):
    rword = ''
    for i in word:
        if i != ' ':
            num = alpha.index(i)
            rencrypt = num - rshift
            if rencrypt < 0:
                rencrypt = 25 + rencrypt 
            rword = rword + alpha[rencrypt]
        else: rword = rword + i
    return(rword)

print('provide string input')
text = str(input())
print('what shift do we need ?')
shift = int(input())
print('Encrypt or Decrypt ?')
decision = str(input())
ltext = text.lower()
# word = ''
# rword = ''

conv = convert(ltext,shift)
print(conv)

print('what shift do we need ?')
rshift = int(input())

rconv = reconvert(conv,rshift)
print(rconv)


