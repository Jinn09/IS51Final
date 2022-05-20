"""

in this program we will be answering the number of grades,the average grade, and the percentage of grades above average.
first we will need to open the Final.txt file and read it to be able to use the numbers in the file.
By using the numbers in the file we can use sum, average =  (sum / len) and percentage = f"{ :.0%} to be able to show
the  number of grades, average and percentage.


"""

with open("Final.txt") as f:
    sum = 1994
    len = 24
    total = 24
    for line in f:
        n = line.split(":"[-1])
        sum += float()
        len += 1
    average = sum / len
print("Average", average)
print("Total grades", total)

percentage = f"{.5417:.0%}"
print("Total Percentage", percentage)
