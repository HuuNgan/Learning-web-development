def square(x):		# define a new function
    return x*x

def main():
    for i in range(10):
        print("{} sqare is {}". format(i, square(i)))

if __name__ == "__main__":
    main()
