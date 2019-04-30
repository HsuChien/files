import time
def x_key():
    x_circle=42
    x=(time.time()-1556500142.4091797)/60/60/24
    if x<=x_circle:
        print(x_circle-x,'欢迎使用')
        return 1
    elif x>x_circle:
        print(x_circle-x,'请联系管理员！')
        return 0


