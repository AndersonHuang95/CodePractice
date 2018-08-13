class Solution:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        HEADER = "***Header: start of message***"
        FOOTER = "***Footer: end of message***"
        encoded_str = ""
        encoded_str += HEADER + "\n"
        for s in strs:
            encoded_str += s + "\n"
        encoded_str += FOOTER + "\n\n"
        print(encoded_str)
        return encoded_str
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        HEADER = "***Header: start of message***"
        FOOTER = "***Footer: end of message***"
        res = []
        if HEADER not in s or FOOTER not in s: 
            raise ValueError("Cannot decode corrupted string")
        
        start_of_header = s.find(HEADER)
        start_of_footer = s.find(FOOTER)
        offset = start_of_header + len(HEADER) + 1
        end = offset
        while end < start_of_footer:
            if s[end] == "\n":
                print(offset, end)
                res.append(s[offset:end])
                offset = end + 1
            end += 1
        return res

def main():
    x = [""]
    sol = Solution()
    enc = sol.encode(x)
    dec = sol.decode(enc)
    print(dec)

if __name__ == '__main__':
    main()