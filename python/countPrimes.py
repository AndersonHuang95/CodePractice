import math

class Solution:
    def countPrimes(self, n):
        """
        To consider this problem, we must define what prime means. 
        A prime number is a number divisble by only itself and one. 

        Naively to enumerate all primes up to n, we do the following: 
        For each number, x, in the range 2 to n: 
            Check if any number in the range 2 to (x - 1) divides -- actually we only need to go up until sqrt(x)
            since sqrt(x), any larger factor will be grouped in by the corresponding complementary smaller factor 

        This results in a lot of wasted work. Instead we can go thru all multiples of each number until sqrt(x)
        which will save us some time... 

        For an arbitrary n, we will consider the follow amount of numbers.

        n / 2 + n / 3 + n / 4 + n / 5 + n / sqrt(n) 

        :type n: int
        :rtype: int
        """
        candidates = [True for _ in range(n)]
        count = 0
        for i in range(2, n):
            if candidates[i] == True: 
                count += 1
                for multiple in range(2 * i, n, i): 
                    candidates[multiple] = False
        return count

def main():
    sol = Solution()
    print(sol.countPrimes(10))

if __name__ == '__main__':
    main()