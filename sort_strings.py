from collections import defaultdict
class SortAlphabetsinString:

    def sort_alphabets_string(self, input_string):
        d = defaultdict()
        for s in input_string:
            if ord(s) in d:
                d[ord(s)].append(s)
            else:
                d[ord(s)]=[s]

        sorted_keys = sorted(d.keys())
        result = ''
        for k in sorted_keys:
            result += ''.join(d[k])
        return result.strip(' ')


if __name__ == "__main__":
    s = "This is a string and I want to accumulate all letters"
    sr = SortAlphabetsinString()
    result = sr.sort_alphabets_string(s)
    print(result)
