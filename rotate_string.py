
class RotateString:

    def rotate(self, string, index, clockwise=True):
        if clockwise:
            left_string = string[0:index]
            right_string = string[index:]
        else:
            left_string = string[0:-index]
            right_string = string[-index:]
        return right_string + left_string


if __name__ == "__main__":
    rs = RotateString()
    s = "Abracadabra"
    result = rs.rotate(s, 3)
    print(result)
    result2= rs.rotate(s, 3, clockwise=False)
    print(result2)
