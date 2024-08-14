# Number of 1 Bits (Easy)
# This solution converts the number into its binary representation and counts the number of '1' bits.
# It loops through each bit in the binary string to calculate the count.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_number = bin(n)[2:]
        print(binary_number) 
        c=0
        for i in binary_number:
            if i=='1':
                c+=1
        return c
