#coding:utf-8
import socket
import Queue
import select
import traceback
import time

class ChatServer():
    def __init__(self):
        self.dict_name = {}#�ͻ���
        self.dict_msg = {}#��Ϣ����
        self.listen_fd = 0#��ʼ���������ļ�������
        self.inputs = []#�ɶ�״̬�б�
        self.outputs = []#��д״̬�б�
    def run(self):
        ''' ��select����socket'''
        s = socket.socket()#Ĭ��ip tcp��Э��
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#��ַ����
        s.bind(('localhost',10001))
        s.listen(1)
        self.inputs.append(s)#��s���뵽�������б� 
        self.listen_fd = s#��Ҫ�������ļ�����������listen_fd
        while True:
            list_r,list_w,list_e = select.select(self.inputs,self.outputs,self.inputs)
            '''
                �����ոմ������ļ���������inputs�б��У�����������ӵ�socket��select��sд��lis_r��
                ��������ݷ��ͼ���lis_w�н��в�����������쳣��lis_e�в���
                ȷ����һ��select��⵽��״̬�϶����¿ͻ������ӽ�����
            '''
            if self.listen_fd in list_r:#���s�ڿ�д״̬�����������ӻ���������
                conn,cli = self.listen_fd.accept()#�½�һ���ļ������� �����пͻ������������ͨ��
                self.dict_name[conn] = '' #�µ��ļ����������뵽�ֵ�
                self.dict_msg[conn] = Queue.Queue()#���ͻ��˼��뵽��Ӧ����Ϣ����
                self.inputs.append(conn) #���µ��ļ����������뵽�����б���
                print 'new connects',conn.getpeername() #getpeername()����ȡ�����ӳɹ�֮ Socket �ĶԷ�λַ�� 
            '''
                ���ӳɹ���ʼ���� select��
            '''
            self.doExcept(list_e)
            self.doRead(list_r)
            self.doWrite(list_w)
            time.sleep(0.1)
    def doRead(self,list_r=[]):
        for ts in list_r:
            if ts is self.listen_fd:continue#����Ǽ�����socket �ͼ���
            try:
                msg = ts.recv(1024) #select��鵽������ʱ �������Ӿ��ǽ�������
                if msg:#���������
                    print 'read[%s]'%msg
                    cmd,tmp = msg.split(None,1)#��һ����ֵ����һ�� �ͻ���cmd �����������
                    print 'split[%s][%s]'%(cmd,tmp) 
                    if cmd == 'name':#�ͻ��˵�½������
                        self.doName(ts,tmp)
                    elif cmd == 'pm':#���͸�ĳ��
                        self.doPm(ts,tmp)
                    elif cmd == 'show':
                        self.doShow(ts,tmp)
                    else:
                        self.doMsg(ts,tmp)
                    if ts not in self.outputs:#׼�����͸��ͻ���
                        self.outputs.append(ts)
                else:
                    self.doExcept([ts])
                print 'read',ts.fileno(),len(msg) #���ļ�������
            except:
                traceback.print_exc()
    def doWrite(self,list_w=[]):
        for ts in list_w:
            try:
                if not self.dict_msg[ts].empty():
                    msg = self.dict_msg[ts].get_nowait()#���ȴ���û��������ֱ�������쳣
                    if msg:
                        ts.send(msg)
                    print 'write',ts.fileno(),len(msg)
            except:
                traceback.print_exc()
    def doExcept(self,list_e=[]):#�쳣�Ĵ���
        for ts in list_e:
            if ts in self.inputs:#����쳣���ټ������������е��ļ�������ɾ��
                self.inputs.remove(ts)
            if ts in self.outputs:
                self.outputs.remove(ts)
            if ts in self.dict_name:
                del self.dict_name[ts]
            if ts in self.dict_msg:
                del self.dict_msg[ts]
            print 'except',ts.fileno()
        
    def doName(self,ts='',tmp=''):#ts���շ��������� tmp ��½������
        self.dict_name[ts] = tmp#�ͻ��˶�Ӧ���͵���Ϣ�����˵�����
        users = [k for k in self.dict_name if self.dict_name[k]] #������ӵĿͻ���������
        for s in self.dict_msg:#��������ÿ����Ϣ���з���һ����Ϣ
            self.dict_msg[s].put('welcome %s, there are %s friends now' % (tmp, len(users))) 

    def doMsg(self,ts='',msg=''):#Ⱥ����Ϣ
        name = self.dict_name[ts]
        for s in self.dict_msg:#�µ��ļ�����������Ϣ������
            self.dict_msg[s].put('from %s:%s'%(name,msg))

    def doShow(self,ts='',msg=''):#�鿴��������
        users = [self.dict_name[k] for k in self.dict_name if self.dict_name[k]]
        if ts in self.dict_msg:
            msg = 'there are %s users\n %s'%(len(users),users)
            self.dict_msg[ts].put(msg)

    def doPm(self,ts='',msg=''):#��ĳ�˷�
        user,tmp = msg.split(None,1)
        find_user = 0
        for s in self.dict_name:
          if self.dict_name[s] == user: #����ĳ�˷�ʱȡ��ĳ�˵���Ϣ����
            self.dict_msg[s].put('from %s:%s' % (self.dict_name[ts], tmp))#�����û��� ��Ϣ 
            find_user = 1
            break
        if not find_user:
            self.dict_msg[ts].put('user [%s] not found, and private msg not sent successfully' % find_user)
           
if __name__=='__main__':
    cs = ChatServer()
    cs.run()
