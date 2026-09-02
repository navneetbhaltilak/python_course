def my_generator():
    for i in range(50000):
        yield i

grn=my_generator()
for i in grn:
    if i==9999:
        print("Number is 9999")
        break

'''
Conclusion on Generators and yield
Generators with yield are powerful because they let you produce values one at a time instead of building everything in memory at once.

They are memory-efficient, lazy (on-demand), and make writing iterators much simpler.

Use them when dealing with large datasets, streams, or infinite sequences where you don’t want to store everything upfront.

Think of them as a tap: you only get water when you open it, instead of filling a giant bucket first.
'''