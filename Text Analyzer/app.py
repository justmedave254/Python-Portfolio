file_n = input("Enter the file name: ")
charac = input("Enter the character you want to count in file: ")

with open(file_n) as f:
    text = f.read()

def char_count(text,charc):
    count = 0
    for c in text:
        if c == charc:
            count += 1
    print(f"The charcter {charc} appears {count} times in the file.\n")

    perc = input("Do you want to find out its percentage in the file? ").lower()
    if perc == 'yes':
        print(str(round(char_perc := 100 * count / len(text),2)) +"%\n")
    elif perc == 'no':
        print("Percentage will not be calculated.\n")
    else:
        print('You can only answer yes or no\n')

    conf = input("Do you want to run it again? ").lower()
    return conf

heh = char_count(text,charac)

while heh == 'yes':
    charac = input("Enter the character you want to count in file: ")
    heh = char_count(text,charac)
else:
    print("Program terminated")