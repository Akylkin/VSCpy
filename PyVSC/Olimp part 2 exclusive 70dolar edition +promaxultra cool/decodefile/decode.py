f = open('0059_cipher.txt')

x = f.read().split(',')

msg = ''

for i in x:
    msg += chr(int(i))


def xordecoder(key: str, txt = '') -> str:
    result = ''
    i = 0
    for c in txt:
        result += chr(ord(c) ^ ord(key[i]))
        i += 1
        if i >= len(key):
            i = 0
    return result

def checkstr(s: str) -> bool:
    check = [' an ', 'An ', ' the ', 'The ', ' is ', 'Is ', ' are ', 'Are ', ' am ', 'Am ', ' to ', 'To ', ' of ', 'Of ', ' and ', 'And ', ' at ', 'At ', ' it ', 'It ']
    a = 0
    for i in check:
        a += s.count(i)
    if(a >= 30):
        return True
    return False

def absolutedecoder(s: str) -> list:
    result = []
    for as1 in range(30, 170):
        for as2 in range(30, 170):
            for as3 in range(30, 170):
                key = str(chr(as1)) + str(chr(as2)) + str(chr(as3))
                txt = xordecoder(key, s)
                if(checkstr(txt)):
                    print('key: ' + key + ' text: ' + txt)
                    result.append('key: ' + key + ' text: ' + txt)
    return(result)

print(absolutedecoder(msg))