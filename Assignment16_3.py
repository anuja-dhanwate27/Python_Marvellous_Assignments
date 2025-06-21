def main():
    print("Enter the file name:")
    FileName = input()
    fobj = open(FileName,"r")
    lines = fobj.readlines()

    line_count = 0
    word_count = 0
    char_count = 0

    for i in lines:
        line_count = line_count + 1
        words = i.split()
        word_count = word_count +len(words)
        char_count = char_count + len(i)

    print("Total Lines :",line_count)
    print("Total woeds:",word_count)
    print("Total characters:",char_count)

if __name__=="__main__":
    main()
    

