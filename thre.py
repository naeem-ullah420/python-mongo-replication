import threading,time
start=time.time()
def hi():
    time.sleep(1)
    print('hi')
# for i in range(10):
#     hi()
threads=[]
for i in range(10):
    threads.append(threading.Thread(target=hi))
for i in threads:
    i.start()
    i.join()
# for i in threads:
#     i.join()



print(time.time()-start)