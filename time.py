import time

start = time.time()

for i in range(10000):
    print(i)
print()
end = time.time()
print(end - start)
time.sleep(20)
