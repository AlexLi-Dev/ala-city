# 封装异常类
class GlobalException(Exception):
    def __init__(self,message,detail=None):
        super().__init__(message)
        self.detail = detail
     
try:
    raise GlobalException('密码错误',"好小子，竟然告我系统")
except Exception as e:
    print(e.detail)