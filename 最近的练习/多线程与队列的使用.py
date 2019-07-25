import requests
from lxml import etree
import threading  # 创建线程
from queue import Queue  # 用队列做数据结构供线程使用

class QiubaiSpdier(object):
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.url_queue = Queue()  # url_list
        self.html_queue = Queue() # HTML
        self.data_queue = Queue() # 需要的信息

    def get_url_list(self):#构造url并存入url队列中
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def get_html(self):#从url队列中取出url，获取HTML并存入HTML队列中
        while True:
            url = self.url_queue.get()

            print('解析:',url)
            # 请求HTML并返回，res.content.decode()
            self.html_queue.put(url)

            self.url_queue.task_done()

    def get_mess_list(self):#从HTML队列中取出HTML，并解析数据存入data队列中
        while True:
            html = self.html_queue.get()
            #解析HTML并提取信息
            mess = html

            self.data_queue.put(mess)
            self.html_queue.task_done()

    def save_mess(self):
        while True:
            data = self.data_queue.get()
            #存储/输出需要的数据
            print('输出:',data)
            self.data_queue.task_done()
        

    def run(self):
        thread_list = []
        #1.获取url
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        #2.获取HTML
        t_html = threading.Thread(target=self.get_html)
        thread_list.append(t_html)
        #3.解析HTML
        t_mess = threading.Thread(target=self.get_mess_list)
        thread_list.append(t_mess)
        #4.保存/输出解析后的信息
        t_save = threading.Thread(target=self.save_mess)
        thread_list.append(t_save)

        for t in thread_list:
            t.setDaemon(True)  # 将进程设置为守护线程，主线程结束，子线程无条件结束
            t.start()

        for q in [self.url_queue, self.html_queue, self.data_queue]:
            q.join()  # 让三个队列事件全部完成之前主线程阻塞

        print("----------end----------")

    

if __name__ == '__main__':
    qiubai = QiubaiSpdier()
    qiubai.run()
