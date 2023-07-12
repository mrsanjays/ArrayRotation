#right rotation of array
class Solution:
    @staticmethod
    def reverse(array,left,right):
        while left<right:
            array[left],array[right]=array[right],array[left]
            left+=1
            right-=1
    """
    Approach:step1: Reverse the whole array
             step2: reverse the array up to 0 to k-1 
             step3: Reverse the array up to k to n-1
    """

    def ArrayRotation(self, array, k):
        n = len(array)
        k = k % n
        self.reverse(array, 0, n - 1)
        self.reverse(array, 0, k - 1)
        self.reverse(array, k, n - 1)

if __name__ == '__main__':
    ob=Solution()
    array=list(map(int,input().split()))
    k=int(input())
    ob.ArrayRotation(array,k)
    print(*array)

""" 
Given an integer array A of size N and an integer K, 
you have to return the same array after rotating it K times towards the right


"""