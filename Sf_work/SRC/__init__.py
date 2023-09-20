import sys

import SRC.main


def get_addr():
    try:
        addr1 = sys.argv[1]
        addr2 = sys.argv[2]
        # 判断是否有从控制台中接收到数据
        if addr1 == "" or addr2 == "":
            raise IndexError
        else:
            SRC.main.diff_seek(addr1, addr2)
            # print(addr1)
            # print(addr2)
            return None
    except IndexError as e:
        print("请你传入,源文件和待检测文件的地址!\n")
