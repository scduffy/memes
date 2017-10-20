def memeify(string):
    memed_string = ""
    string = string.lower()
    string = string.strip()
    for i in range(len(string)):
        if string[i] == " " or string[i] == "?" or string[i] == "!" or string[i] == "." or string[i] == "\"" or string[i] == "," or string[i] == "'" or string[i] == "’" or string[i] == ":" or string[i] == ";" or string[i] == "-":
            memed_string = " " + memed_string
        elif string[i] == "b":
            memed_string = memed_string + " :b:"
        else:
            memed_string = memed_string + " :regional_indicator_" + string[i] + ":"
    return memed_string


def slicer_loop(memed_string):
    i = 0
    while i*2000 <= len(memed_string):
        string = memed_string[i*2000:2000+(i*2000)]
        print('\n' + string)
        i += 1


def main():
    string = str(input("What do you want to translate"))
    string = memeify(string)
    slicer_loop(string)


main()