"""
1.Write a program that:
  Prints numbers from 1 to 20.
  Skips multiples of 3 using continue.
  Stops when the number reaches 18 using break.
"""
for i in range(1, 21):
    if i % 3 == 0:
        continue
    if i > 18:
        break
    print(i)