# File handling - Even and Odd numbers
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# open numbers.txt (read), open even.txt (append), open odd.txt (append)
with open("numbers.txt") as input_file, open("even.txt", "a") as output_even, open("odd.txt", "a") as output_odd:
    # read numbers.txt line by line
    for line in input_file:
        int_line = int(line)
        print(int_line)
        # if even
            # append even numbers to even.txt
        # if odd
            # append odd numbers to odd.txt
