#电子时钟
import time
while True:
  
    # sj = time.localtime()
    sj = time.asctime()

    # print(sj[3],sj[4],sj[5],sep=':')
    print(sj[11:-5],end = '\r')
    time.sleep(1)















