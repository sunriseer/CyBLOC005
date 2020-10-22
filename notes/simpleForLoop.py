"""
PI = 3.14159
return 4 * PI * (radius ** 2)

#######################################

return False if 223 >= int(addr.split('.')[0]) >= 240 else True

#######################################

return [i for i in range(0, 1024)]

#######################################

if number[0] == 'z':
    return 0
elif number[0] == 'o':
    return 1
elif number[0] == 't':
    if number[1] == 'w':
        return 2
    else:
        return 3
else:
    return 4

#######################################

data = input("Enter an number: ")
temp = []

for i in range(len(data)):
    if data[i].isdigit():
        temp.append(data[i])

return int(''.join(temp))

#######################################

print("{}.{}.{}@{}.com".format(first, middle[0], last, domain))

#######################################

with open(infile, "r") as fin, open(outfile, "w") as fout:
    fout.writelines(fin.readlines())

#######################################

return tuple('.'.join(address.split('@')).split('.')[:4])

#######################################

dict = {}

for char in strng:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

return dict

#######################################

return ('McMillen', 'nelliMcM')

#######################################

s = socket.socket()

try:
    s.connect((address, port))
except:
    return False

return True

#######################################

sum = 0

    for arg in args:
        sum += arg

    for key, arg in kwargs.items():
        sum += arg

    return sum

#######################################

msg = bytearray()

    s = socket.socket()
    s.connect((address, port))
    s.sendall(b'hello')

    echodata = s.recv(4096)
    return echodata

#######################################

class car:
    def __init__(self):
        self.speed = 0

    def setspeed(self, speed):
        self.speed = speed

    def getspeed(self):
        return self.speed

    def speedup(self):
        self.speed += 1

    def slowdown(self):
        self.speed -= 1

    def stop(self):
        self.speed = 0

    def __str__(self):
        return "Current speed: {}".format(self.speed)

#######################################



#######################################

"""