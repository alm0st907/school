#python 3
#garrett rudisill
def other():
    print("seeing if another function gets auto executed")
def main():
    #the code goes here
    print("hello world")
    string = input("Type a string here")
    string = string.split(',')
    for word in string:
        print(word)


if __name__ == "__main__":
    main()