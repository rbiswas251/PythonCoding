
class RotateString:

    def rotate_brute_force(self, string, index, clockwise=True):
        if clockwise:
            left_string = string[0:index]
            right_string = string[index:]
        else:
            left_string = string[0:-index]
            right_string = string[-index:]
        return right_string + left_string

    def rotate_recursive(self, str_, index, clockwise=True):

        if clockwise:
            return self.__rotate(str_, index)
        else:
            return self.__rotate(str_, len(str_)-index)

    def __rotate(self, str_, index):
        temp_string = str_ + str_
        temp = temp_string[index: index + len(temp_string)]
        return temp[:len(str_)]


if __name__ == "__main__":
    rs = RotateString()
    s = "GeeksforGeeks"
    result = rs.rotate_brute_force(s, 3)
    print(result)
    result2= rs.rotate_brute_force(s, 3, clockwise=False)
    print(result2)

    result3 = rs.rotate_recursive(s, 3)
    print(result3)
    result4 = rs.rotate_recursive(s, len(s)-3)
    print(result4)
