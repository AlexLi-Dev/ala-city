from wsgiref import headers

from rest_framework.response import Response

class APIResponse(Response):
    def __init__(self, code=100,msg='success',status=200,headers={},**kwargs):
        msg = 'failed' if code not in  [100,200] else 'success'
        data = {
            'auth-devoper':'lutong.li',
            'code': code,
            'msg': msg,
        }
        if kwargs:
            data.update(kwargs)
        super().__init__(data=data,status=status,headers=headers)