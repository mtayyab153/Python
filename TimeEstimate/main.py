import time

start = time.time()
for i in range(1, 100000):
    print(i)
end = time.time()

print("Time: ", end - start)

# from timeit import default_timer as timer
#
# start = timer()
#
# for i in range(1, 100000):
#     print(i)
#
# end = timer()
# print(end - start)
