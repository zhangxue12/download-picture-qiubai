#期末项目，抓取糗百热图
import os
import urllib.request
import _thread
import time
import threading
import requests
import re
def down_load_page(url,start_page):
	global cnt_download
	#lock.acquire()
	i= 1
	req = requests.get(url)
	data = req.text
	pic_list = re.findall(r"\S+.jpeg",data)
	path = "hot-picture\\"
	if os.path.exists(path):
		pass
	else :
		os.mkdir(path)
	for pic in pic_list:
		pic2 = re.findall(r"pic\S+",pic)
		url = "http://"+pic2[0]
	path = "hot-picture\\"+"page-"+str(start_page)
	if os.path.exists(path):
		pass
	else :
		os.mkdir(path)
	
	for pic in pic_list:
		pic2 = re.findall(r"pic\S+",pic)
		url = "http://"+pic2[0]
		
		req_pic = urllib.request.urlopen(url)
		data_pic = req_pic.read()
		str1= str(i)
		name = "f1-i"
		with open(path+"\\"+str1+".jpeg","wb") as name:
			name.write(data_pic)
		print("page%d--%d.jepg is finish"%(start_page,i))
		i+=1
	cnt_download += 1
	#lock.release()

def input_judge():  
    '''输入并判断'''
    i = 5
    num_list = [k for k in range(1,14)]
    while i>0: 
        try:
        	start_page = eval(input("请输入抓取起始页码： "))
        	stop_page = eval(input("请输入结束页码： "))
        except (NameError,SyntaxError):
            print("输入错误，请重新输入！")
            print("=====================")
            i -= 1 
            continue
        else :
            if (start_page not in num_list) or \
                (stop_page not in num_list) and i != 1:
                print("输入的页码不在范围内，请重新输入！")
                print("=====================")
                i -= 1
                continue
            elif (start_page in num_list) and \
                (stop_page in num_list):
            	if stop_page < start_page:
            		print("结束页码大于起始页码，请重新输入！")
            		print("=====================")
            		continue
            	else :
            		break
    if i == 0:
        print("你已经连续输错5次，程序自动退出！")
        exit(0)
    else :
        return start_page,stop_page
   

lock = threading.Lock()
cnt_download= 0
def main():
	global cnt_download
	print("*****欢迎使用糗百热图下载程序*******")
	while True:
		cnt_download = 0
		print("请输入你要下载糗百热图的页码，共有13页!")
		start_page,stop_page = input_judge()
		cnt = stop_page - start_page+1
		url_list = []
		for page in range(start_page,stop_page+1):
			url_add = r"https://www.qiushibaike.com/imgrank/page/"+str(page)+"/"
			url_list.append(url_add)	
		threadings = []
		start_page1 = start_page
		for url in url_list:
			t = threading.Thread(target=down_load_page,args=(url,start_page1))
			threadings.append(t)
			start_page1 += 1 
		start_time = time.time()
		for k in threadings:
				k.start()
		while True:
			if cnt_download == cnt:
				print("下载耗时：%f"%(time.time()-start_time))
				print("\n********图片下载完成*************\n")
				c = input("按任意键继续，\n退出请输入 2 \n")
				if c == "2":
					exit(0)
				else:
					break
			else:
				continue
		
if __name__ == '__main__':
	main()
