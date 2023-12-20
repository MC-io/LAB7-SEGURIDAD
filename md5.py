import struct
import math


class MD5:
    def F(self, X, Y, Z):
        return (X & Y) | (~X & Z)

    def G(self, X, Y, Z):
        return (X & Z) | (Y & ~Z)

    def H(self, X, Y, Z):
        return X ^ Y ^ Z

    def I(self, X, Y, Z):
        return Y ^ (X | ~Z)

    def rotate_left(self, value, shift):
        return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

    def pad_message(self, message):
        original_length = len(message) * 8
        message += b'\x80'
        while (len(message) * 8) % 512 != 448:
            message += b'\x00'
        message += struct.pack('<Q', original_length)
        return message

    def digest(self, message):
        message = message.encode('utf-8')
        A = 0x67452301
        B = 0xEFCDAB89
        C = 0x98BADCFE
        D = 0x10325476

        # Constants
        K = []
        for i in range(64):
            K.append(int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF)


        message = self.pad_message(message)

        # Process each block
        for block_start in range(0, len(message), 64):
            block = message[block_start:block_start+64]

            M = struct.unpack('<16I', block)

            AA = A
            BB = B
            CC = C
            DD = D

            for i in range(64):
                if i < 16:
                    F_result = self.F(BB, CC, DD)
                    g = i
                    s = [7, 12, 17, 22][i % 4]
                elif i < 32:
                    F_result = self.G(BB, CC, DD)
                    g = (5 * i + 1) % 16
                    s = [5, 9, 14, 20][i % 4]
                elif i < 48:
                    F_result = self.H(BB, CC, DD)
                    g = (3 * i + 5) % 16
                    s = [4, 11, 16, 23][i % 4]
                else:
                    F_result = self.I(BB, CC, DD)
                    g = (7 * i) % 16 
                    s = [6, 10, 15, 21][i % 4]

                F_result = (F_result + AA + K[i] + M[g]) & 0xFFFFFFFF
                AA = DD
                DD = CC
                CC = BB
                BB = (BB + self.rotate_left(F_result, s)) & 0xFFFFFFFF

            A = (A + AA) & 0xFFFFFFFF
            B = (B + BB) & 0xFFFFFFFF
            C = (C + CC) & 0xFFFFFFFF
            D = (D + DD) & 0xFFFFFFFF

        result = struct.pack('<4I', A, B, C, D)
        return result.hex()