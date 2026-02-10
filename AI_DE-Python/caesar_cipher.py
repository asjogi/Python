alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

input_given = str(input('What is the statement ?'))
delay = int(input("Move it by ?"))
direction = str(input('Encode or Decode ?'))
decision = 'Y'

advanced_string = []
output_del = ''
def encode(input_given, delay: int):
    output_del = ''
    for value in input_given:
        if value not in alphabets:
            output_del += value
        elif value == ' ':
            output_del += ' '
        else:
            new_value = alphabets.index(value) + delay
            new_value = new_value % 25
            output_del += alphabets[new_value]
    return output_del

def decode(input_given, delay: int):
    output_del = ''
    for value in input_given:
        if value not in alphabets:
            output_del += value
        else:
            new_value = alphabets.index(value) - delay
            new_value = new_value % 25
            output_del += alphabets[new_value]
    return output_del
# print(encode('how', 5))
# out_value = decode('mtc g', 5)
# for value in advanced_string:
#     output_del += output_del.join(value)
# output_del = decode('mtc nx9', 5)
# output_del = encode('how is9', 5)
# print(output_del)

while decision == 'Y':
    if direction == 'encode':
        print(encode(input_given,delay))
    else: 
        print(decode(input_given,delay))
    decision = input("Do you want to continue Y/N ?")
    if decision == 'Y':
        input_given = str(input('What is the statement ?'))
        delay = int(input("Move it by ?"))
        direction = str(input('Encode or Decode ?'))
    else: break

