#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseResponse(object):
    """
        基础相应信息类
    """
    def __init__(self):
        self.status = True
        self.message = None
        self.data = None
        self.error = None
