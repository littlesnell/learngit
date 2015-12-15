#coding:utf-8
import cmd, socket, traceback, threading, time
import sys
def inBlack(s):
    return highlight('') + "%s[30;2m%s%s[0m"%(chr(27), s, chr(27))
def inRed(s):
    return highlight('') + "%s[31;2m%s%s[0m"%(chr(27), s, chr(27))
def inGreen(s):
    return highlight('') + "%s[32;2m%s%s[0m"%(chr(27), s, chr(27))
def inYellow(s):
    return highlight('') + "%s[33;2m%s%s[0m"%(chr(27), s, chr(27))
def inBlue(s):
    return highlight('') + "%s[34;2m%s%s[0m"%(chr(27), s, chr(27))
def inPurple(s):
    return highlight('') + "%s[35;2m%s%s[0m"%(chr(27), s, chr(27))
def inWhite(s):
    return highlight('') + "%s[37;2m%s%s[0m"%(chr(27), s, chr(27))
def highlight(s):
    return "%s[30;2m%s%s[1m"%(chr(27), s, chr(27))
class ChatClient(cmd.Cmd):
    ''' chat client '''
    def __init__(self, host='localhost', port=10001):
        cmd.Cmd.__init__(self)
        self.host = host
        self.port = port
        self.sock = ''
        self.prompt =  inRed('chatClient>')
        self.completekey='\n'
        self.name = ''
        
    def do_connect(self, line):#���ӵ�server
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((self.host, self.port))
        s.settimeout(0.1)#���ó�ʱʱ�� 0.1 ��
        print inGreen('you are connected, and you can input your name, example: name Vincent')
        self.sock = s
   
    def do_name(self, line):
        if not self.sock:#�ȵ����Ӳ���ִ�С�
            print inRed('please connect first')
        line = line.strip()
        self.prompt = inGreen('%s>' % line)
        self.sock.send('name\t%s' % line)#��������
        self.name = line
        #print 'name', line
        t = threading.Thread(target=ChatClient.continue_read, args=(self,))#����һ�����̡߳�
        t.setDaemon(True)#�ػ��߳������߳�û��ִ�����ʱ����򲻻ᱻ�˳�
        t.start()
	'''
		������⣺
		setDaemon(True)���߳�����Ϊ�ػ��̣߳�������start() ��������֮ǰ���ã����������Ϊ�ػ��̳߳���ᱻ���޹���
		The entire Python program exits when no alive non-daemon threads are left					
		������仰����˼�ǣ���û�д��ķ��ػ�����ʱ������python����Ż��˳���
		Ҳ����˵��������߳�ִ�����Ժ�,�����������ػ��߳�,���߳��ǲ����˳���
		���ᱻ���޹��𣻱��뽫�߳�����Ϊ�ػ��߳�֮����������е������������ˣ���ô����������ʲôʱ���˳����˳������õȴ���
		'''
        
    def do_msg(self, line):
        if not line:
            print inRed('input error, msg is empty, check it and reinput')
        if line:
            self.sock.send('msg\t%s' % line)
    
    def do_show(self, line):
        if not self.name:
            print inRed('please set your name first')
        self.sock.send('show\ttmp')#����show ��tmp
        #print 'show'
        
    def do_pm(self, line):
        if not line:
            print inRed('input error, msg is empty, check it and reinput')
        if line:
            self.sock.send('pm\t%s' % line)
            
    @staticmethod#����self  �޷����ʳ�Ա���� �ҿ���ֱ�ӵ��ò��üӲ���
    def continue_read(chatclient):#���շ��ص���Ϣ���Ҵ�ӡ����
        while 1:
            try:
                msg = chatclient.sock.recv(1024) #�½�����
                if msg:
                    print inGreen(msg)
                    sys.stdout.write(chatclient.prompt)
                    sys.stdout.flush()
                else:
                    break
            except socket.timeout:
                pass
            except:
                traceback.print_exc()
            time.sleep(1)
        print inRed('exit thread'), inBlue(threading.currentThread().getName())#�鿴��ǰ���߳�����
       
    def do_EOF(self, line):#�˳�
        if self.sock:
            self.sock.close()
        return True
    
    
if __name__=='__main__':
    info='''
                     help:
        1.connect         ---  ���ӵ�������
        2.name [vincent]  ---  ���ǳƵ�½
        3.show            ---  �鿴��ǰ��������
        4.msg [message]   ---  Ⱥ����Ϣ
        5.pm [vincent] [message]  --- ���͸�ĳ��
        '''
    print inPurple(info)
    ChatClient().cmdloop()
