class ReverseString:

    def string_reverse_bruteforce(self, string):
        n = len(string)
        result = ''
        for i in range(1, n+1, 1):
            result += string[-i]
        return result

    def string_reverse_inplace(self, string):
        """
        This has Time Complexity O(n)
        Space complexity O(1)asw3
        """
        string_list = list(string)
        n = len(string_list)
        i, j = 0, n-1
        while i < j:  # You don't want to cross
            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1
        result = ''.join(string_list)
        return result


if __name__ == "__main__":
    sr = ReverseString()
    s = "This is very good"
    print(s)
    result = sr.string_reverse_bruteforce(s)
    result2 = sr.string_reverse_inplace(s)
    print(result)
    print(result2)


