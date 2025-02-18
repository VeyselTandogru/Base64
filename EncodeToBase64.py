input_string = "istanbul"
def ascii_to_8bit(input_string):
    ASCII = []
    binary = []
    for i in range(len(input_string)):
        ASCII.append(ord(input_string[i]))
        binary.append(format(ASCII[-1], '08b'))
        
    return(binary)

strBinary = ""
def bit_to_ascii(strBinary, flag):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    count = []
    for i in strBinary:
        if len(count) == 0 or len(count[-1]) == 6: 
            count.append("")  
        count[-1] += i  
    base64_result = "".join(base64_chars[int(bits, 2)] for bits in count)
    if flag:
        base64_result+="="
    return base64_result

x = 0
flag = False
strBinary = "".join(ascii_to_8bit(alınanDeger))
if len(strBinary)%24 != 0:
    x, flag = [(24 - len(strBinary)%24), False] if (24 - len(strBinary)%24) < 6 else [(24 - len(strBinary)%24) - 6, True]
    for i in range(x):
        strBinary += "".join("0")

print(bit_to_ascii(strBinary, flag))