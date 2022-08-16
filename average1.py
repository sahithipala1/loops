def main():
    n = eval(input("How many numbers do you have? "))
    sum = 0.0
    for i in range(n):
        x = eval(input("Enter the number >> "))
        sum = sum + x
    
    print("\n The average of the numbers is", sum / n)


main()
