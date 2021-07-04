# Write a function “sum_evens(to_num)” to calculate the sum of the even numbers
# from 0 to the value of “to_num” passed to the function. Return the sum from the function.
# Call the function inside print to see the result
import sys
def sums_evens(to_num):
    i = 0
    sum =0
    while i < to_num+1:
        if i%2 == 0:
            sum += i
        i+=1
    return sum
to_num = sys.argv[1]
print(sums_evens(to_num))


