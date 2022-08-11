import time

start = time.time()

for i in range(10**3):
    pass

end = time.time()

print(f"time elapsed: {end - start:.10f}sec")