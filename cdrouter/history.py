#
# Copyright (c) 2017 by QA Cafe.
# All Rights Reserved.
#

class History(object):
    RESOURCE = 'history'
    BASE = '/' + RESOURCE + '/'

    def __init__(self, service):
        self.service = service
        self.base = self.BASE

    def list(self, filter=None, sort=None, limit=None, page=None):
        return self.service.list(self.base, filter, sort, limit, page)
