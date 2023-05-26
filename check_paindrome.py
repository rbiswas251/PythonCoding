from collections import Counter
import re
class CheckPalindrome:

    def is_palindrome(self, input_text):
        # Lower the alphabets
        input_text = re.sub(r'[^\w\s]', '', input_text)
        input_text_lower = input_text.lower()
        # Strip of white spaces
        input_text_clean = [i for i in input_text_lower.lower() if i != ' ']  # O(n)
        mid_point = len(input_text_clean)//2
        for i in range(0, mid_point, 1): # O(n/2)
            try:
                assert input_text_clean[i] == input_text_clean[-i-1]
            except AssertionError:
                return False
        return True

    def is_palindrome_frequency(self, input_string):
        input_string = re.sub(r'[^\w\s]', '', input_string)
        input_text_lower = input_string.lower()
        # Strip of white spaces
        input_text_clean = [i for i in input_text_lower.lower() if i != ' ']  # O(n)
        char_count = Counter(input_text_clean)
        odd_count = sum(count % 2 == 1 for count in char_count.values())
        return odd_count <= 1


if __name__ == "__main__":
    cp = CheckPalindrome()
    input_string = "Madam, I'm Adam"
    result = cp.is_palindrome(input_string)
    print(result)
    result = cp.is_palindrome_frequency(input_string)
    print(result)