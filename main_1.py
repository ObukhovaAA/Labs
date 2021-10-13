import sys
def read_from_stdin():
    res = ""
    for line in sys.stdin:
        for word in line.split():
            if word == "End":
                return res
            if int(word) == -1:
                res += " "
            else:
                if int(word) < 6:
                    res += chr(ord('а') + int(word))
                if int(word) == 6:
                    res += 'ё'
                if int(word) > 6:
                    res += chr(ord('а') + int(word) - 1)
if __name__ == '__main__':
    print(read_from_stdin())

