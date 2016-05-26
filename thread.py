import threading
import os
class wal(threading.Thread):
    def run(self):
        j=os.listdir(threading.currentThread().getName())
        for k in j:
            q=threading.currentThread().getName()+'/'+k
            if(os.path.isdir(q)==True):
                print('{0}\n'.format(k))
                x=wal(name=q)
                x.start()
            else:
                print('{0}\n'.format(k))
x=wal(name='c:/Users/Prateek Agarwal/Videos/bollywood')
x.start()
