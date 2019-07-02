import psutil
import tkinter
#An example of a program which requires psutil and tkinter to opperate
print("Example:")
print(psutil.cpu_percent(interval=1))
print(psutil.cpu_percent(interval=1, percpu=True))
print(psutil.sensors_temperatures())
tkinter._test()
