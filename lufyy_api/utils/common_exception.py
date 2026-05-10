
from rest_framework.views import exception_handler
from .common_logger import logger
from rest_framework.response import Response
def common_exception_handler(exc, context):
    # 1 记录日志--》只要是到这里，就是出异常了--》记录日志方便后期排查
    request=context.get('request')
    view=context.get('view')
    # '用户【】，访问地址【】，请求方式是【】，访问视图类【】，错误是【】'
    user = request.user.username or '匿名用户'
    path = request.get_full_path()
    method = request.method
    logger.error(f'用户【{user}】，访问地址【{path}】，请求方式是【{method}】，访问视图类【{str(view)}】，错误是【{str(exc)}】')
    # 2 统一返回格式
    res=exception_handler(exc,context) # 只会处理drf的异常
    res_dict={'code':999,'msg':'系统错误，请联系系统管理员'}
    if res:
        # 说明是drf的异常，它统一处理了
        if isinstance(res.data,dict):
            msg = res.data.get('detail') or res.data or '服务器异常，请联系系统管理员'
        elif isinstance(res.data,list):
            msg = res.data[0]

        res_dict['code']=998
        res_dict['msg']=msg
    else:
        # 非drf异常，没处理，我们需要处理
        msg=str(exc)
        res_dict['code'] = 997
        res_dict['msg'] = msg

    return Response(res_dict)


class PasswordError(Exception):
    def __init__(self,msg,detail='默认参数'):
        super().__init__(msg)
        self.detail=detail