class Solution(object):
    def addBinary(self, a, b):
        # convert binary string into 'int'
        num_a = int(a, 2)
        num_b = int(b, 2)

        total = num_a + num_b

        # convert int back to binary string
        # but since converting will add "0b" prefix, so do [2:] to slice it off
        return bin(total)[2:]
