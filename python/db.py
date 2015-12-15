#!/usr/bin/env python
# coding=utf-8
#db.py

from transwarp import db 
db.create_engine(user='root',password='111111',database='littlesnail',host='127.0.0.1',port=3306)
users = db.select('select * from user')
n = db.update('insert into user(id,name) values(?,?)',4,'Jack')
with db.connection():
    db.select('...')
    db.update('...')
    db.update('...')
#数据库引擎对象：
class _Engine(object):
    def __init__(self,connect):
        self.connect = connect
    def connect(self):
        return self.connect()
engine = None
#持有数据库连接的上下文对象：
class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transactions = 0
    def is_init(self):
        return not self.connection is None
    def init(self):
        self.connection = LasyConnection()
        self.transactions = 0
    def cleanup(self):
        self.connection,cleanup()
        self.connection = None
    def cursor(self):
        return self.connection.cursor()
_db_ctx = DbCtx()
class _ConnectionCtx(objectect):
    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self
    def __exit__(self,exctype,excvalue,traceback):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()
def connection():
    return _ConnectionCtx()
@with_connection
def do_some_db_operation():
    pass
@with_connection
def select(sql,*args):
    pass
@with_connection
def update(sql,*args):
    pass
@with_transaction
def do_in_transaction():
    pass
class _TransactionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_close_conn = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_close_conn = True
        _db_ctx.transactions = _db_ctx.transactions + 1
        return self
    def __exit__(self,exctype,excvalue,traceback):
        global _db_ctx
        _db_ctx.transactions = _db_ctx.transactions - 1
        try:
            if _db_ctx.transactions == 0:
                if exctype is None:
                    self.commit()
                else:
                    self.rollback()
        finally:
            if self.should_close_conn:
                _db_ctx.cleanup()
    def commit(self):
        global _db_ctx
        try:
            _db_cts.connection.commit()
        except:
            _dbctx.connection.rollback()
            raise
    def rollback(self):
        global _db_ctx
        _dbctx.connection.rollback()
