# Use continue to skip even numbers from 1–10.

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)