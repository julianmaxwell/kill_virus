import time
import pandas
from datetime import datetime
from multiprocessing import Process
import psutil
import os
import signal

ok_process_path = r"D:\kill_virus\killdata.csv"
kill_log_path = r"D:\kill_virus\kill_log.csv"
LOG_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

try:
    ok_process = pandas.read_csv(ok_process_path, encoding="gbk").values[:, 0]
except FileNotFoundError as e:
    print("ok_process.csv文件不存在!")
    ok_process = []
except pandas.errors.EmptyDataError:
    print("ok_process.csv文件为空!")
    ok_process = []


def kill_process():
    while True:
        pids = psutil.pids()
        for pid in pids:
            try:
                p = psutil.Process(pid)
            except psutil.AccessDenied:
                continue

            try:
                p.exe()
            except Exception as e:
                print(e)

            if p.name() in ("baidunetdisk.exe", "SGTool.exe", "baidunetdiskhost.ex") or p.name() not in ok_process:
                # print("{} is been killed ,beautiful, file path is {}".format(p.name(), p.exe()))
                try:
                    os.kill(pid, signal.SIGKILL)
                    now = datetime.now().strftime(LOG_TIME_FORMAT)
                    data = pandas.DataFrame([[p.name(), p.exe(), now]])
                    try:
                        data.to_csv(kill_log_path, index=False, header=["进程名", "文件路径", "时间"])
                    except FileNotFoundError as e:
                        print("kill_log.csv文件不存在,正在创建...")
                        data.to_csv(kill_log_path, index=False, header=["进程名", "文件路径", "时间"])
                    except PermissionError as e:
                        print("没有写入kill_log.csv的权限!")
                except Exception as e:
                    pass

        time.sleep(10)


if __name__ == "__main__":
    x = Process(target=kill_process)
    x.start()