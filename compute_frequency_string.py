class ComputeStringFrequency:


    def return_frequency(self, inout_string):
        count_chars = {}
        for ch in inout_string:
            if ch in count_chars:
                count_chars[ch] += 1
            else:
                count_chars[ch] = 1
        return count_chars


if __name__ == "__main__":
    s = "aaaaaaccdeeeghiiillllmnnnorrssssttttttuuw"
    cf = ComputeStringFrequency()
    result = cf.return_frequency(s)
    final_string = ''
    for item, value in result.items():
        final_string += item+str(value)

    print(final_string)