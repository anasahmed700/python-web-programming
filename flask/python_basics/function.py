def square(x):
    return x**2

def main():    
    for i in range(1, 6):
        print("{} squared is {}".format(i, square(i)))


if __name__ == "__main__":
    main()