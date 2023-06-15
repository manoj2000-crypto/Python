# Write a python program to read contents of a file and copy only the content of odd lines into new file.
file = open('Prac1.py', 'r')
file1 = open('test.txt', 'w')
cnt = file.readlines()
type(cnt)
for i in range(0, len(cnt)):
    if i % 2 != 0:
        file1.write(cnt[i])
    else:
        pass

file1.close()
file1 = open('test.txt', 'r')
cnt1 = file1.read()
print(cnt1)
file.close()
file1.close()
