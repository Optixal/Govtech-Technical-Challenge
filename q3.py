#!/usr/bin/python3
# Shawn Pang

from binascii import unhexlify

challenge = [1,0,2,1,0,2,0,0,1,2,3,0,1,2,3,3,1,3,1,2,1,2,1,1,0,2,0,0,1,3,0,0,1,3,0,2,1,2,3,3,1,2,1,3,1,3,0,2,1,2,0,1,1,2,3,1,1,2,3,1,1,2,2,1,1,2,3,2,1,2,1,3]
challengeDecimal = 0

for i in range(1, len(challenge) + 1):
    challengeDecimal += challenge[-i] * (4 ** (i - 1))

print('Challenge in Decimal: {}'.format(challengeDecimal))
challengeHex = str(hex(challengeDecimal)).replace('0x', '')
print('Challenge in Hex:     {}'.format(challengeHex))
challengeASCII = unhexlify(challengeHex)
print('Challenge in ASCII:   {}'.format(challengeASCII.decode('utf-8')))
