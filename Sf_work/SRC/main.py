import difflib
import subprocess
import sys


# 计算文本相似度
def diff_seek(addr_orig: str, addr_add: str):
    # addr_orig, addr_add = get_addr()
    try:
        with open(addr_orig, 'r', encoding='utf-8') as file1:
            lines = file1.read()
        with open(addr_add, 'r', encoding='utf-8') as file2:
            lines2 = file2.read()
    except FileNotFoundError as e:
        print("输入的文件路径错误!!请重新输入!\n")
        return None
        # 比较两个文本相似度
        # 过滤掉不需要比较的字符
    diff = difflib.SequenceMatcher(lambda x: x in [',', '.', ';', ' ', '?', '!', '\n'], lines, lines2).ratio()
    # 将结果写入文件中
    try:
        with open('./diff.txt', 'w', encoding='utf-8') as file:
            file.write("两文本的相似度是: " + str(diff))
        # 调用subprocess模块, 启动系统默认程序打开该文件
        subprocess.call(['start', './diff.txt'], shell=True)  # for Window
    except FileNotFoundError as e:
        print("文件更新失败!!更新失败!!\n")
        return None


# 从控制台中获取参数
def get_addr():
    try:
        addr1 = sys.argv[1]
        addr2 = sys.argv[2]
        # 判断是否有从控制台中接收到数据
        if addr1 == "" or addr2 == "":
            raise IndexError
        else:
            diff_seek(addr1, addr2)
            # print(addr1)
            # print(addr2)
            return None
    except IndexError as e:
        print("请你传入,源文件和待检测文件的地址!\n")


if __name__ == '__main__':
    get_addr()
