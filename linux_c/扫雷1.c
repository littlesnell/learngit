#include <graphics.h>
#include <stdlib.h>
#include <dos.h>
#define LEFTPRESS 0xff01
#define LEFTCLICK 0xff10
#define LEFTDRAG 0xff19
#define MOUSEMOVE 0xff08
struct
{
   int num;/*���ӵ�ǰ����ʲô״̬,1���ף�0�Ѿ���ʾ�����ֻ��߿հ׸���*/
   int roundnum;/*ͳ�Ƹ�����Χ�ж�����*/
   int flag;/*�Ҽ�������ʾ����ı�־,0û�к����־,1�к����־*/
}Mine[10][10];
int gameAGAIN=0;/*�Ƿ������ı���*/
int gamePLAY=0;/*�Ƿ��ǵ�һ������Ϸ�ı�־*/
int mineNUM;/*ͳ�ƴ�����ĸ�����*/
char randmineNUM[3];/*��ʾ���ֵ��ַ���*/
int Keystate;
int MouseExist;
int MouseButton;
int MouseX;
int MouseY;
void Init(void);/*ͼ������*/
void MouseOn(void);/*�������ʾ*/
void MouseOff(void);/*���������*/
void MouseSetXY(int,int);/*���õ�ǰλ��*/
int  LeftPress(void);/*�������*/
int  RightPress(void);/*����Ҽ�����*/
void MouseGetXY(void);/*�õ���ǰλ��*/
void Control(void);/*��Ϸ��ʼ,����,�ر�*/
void GameBegain(void);/*��Ϸ��ʼ����*/
void DrawSmile(void);/*��Ц��*/
void DrawRedflag(int,int);/*��ʾ����*/
void DrawEmpty(int,int,int,int);/*���ֿո��ӵ���ʾ*/
void GameOver(void);/*��Ϸ����*/
void GameWin(void);/*��ʾʤ��*/
int  MineStatistics(int,int);/*ͳ��ÿ��������Χ������*/
int  ShowWhite(int,int);/*��ʾ�������Ŀհײ���*/
void GamePlay(void);/*��Ϸ����*/
void Close(void);/*ͼ�ιر�*/
void main(void)
{
   Init();
   Control();
   Close();
}
void Init(void)/*ͼ�ο�ʼ*/
{
   int gd=DETECT,gm;
   initgraph(&gd,&gm,"c:\\tc");
}
void Close(void)/*ͼ�ιر�*/
{
   closegraph();
}
void MouseOn(void)/*�������ʾ*/
{
   _AX=0x01;
   geninterrupt(0x33);
}
void MouseOff(void)/*���������*/
{
   _AX=0x02;
   geninterrupt(0x33);
}
void MouseSetXY(int x,int y)/*���õ�ǰλ��*/
{
   _CX=x;
   _DX=y;
   _AX=0x04;
   geninterrupt(0x33);
}
int LeftPress(void)/*����������*/
{
   _AX=0x03;
   geninterrupt(0x33);
   return(_BX&1);
}
int RightPress(void)/*����Ҽ�����*/
{
   _AX=0x03;
   geninterrupt(0x33);
   return(_BX&2);
}
void MouseGetXY(void)/*�õ���ǰλ��*/
{
   _AX=0x03;
   geninterrupt(0x33);
   MouseX=_CX;
   MouseY=_DX;
}
void Control(void)/*��Ϸ��ʼ,����,�ر�*/
{
   int gameFLAG=1;/*��Ϸʧ�ܺ��ж��Ƿ����¿�ʼ�ı�־*/
   while(1)
   {
      if(gameFLAG)/*��Ϸʧ�ܺ�û�жϳ����¿�ʼ�����˳���Ϸ�Ļ��ͼ����ж�*/
      {
	 GameBegain(); /*��Ϸ��ʼ����*/
	 GamePlay();/*������Ϸ*/
	 if(gameAGAIN==1)/*��Ϸ�����¿�ʼ*/
	 {
	    gameAGAIN=0;
	    continue;
	 }
      }
   MouseOn();
   gameFLAG=0;
   if(LeftPress())/*�ж��Ƿ����¿�ʼ*/
   {
      MouseGetXY();
      if(MouseX>280&&MouseX<300&&MouseY>65&&MouseY<85)
      {
	 gameFLAG=1;
	 continue;
      }
   }
   if(kbhit())/*�ж��Ƿ񰴼��˳�*/
      break;
   }
   MouseOff();
}
void DrawSmile(void)/*��Ц��*/
{
   setfillstyle(SOLID_FILL,YELLOW);
   fillellipse(290,75,10,10);
   setcolor(YELLOW);
   setfillstyle(SOLID_FILL,BLACK);/*�۾�*/
   fillellipse(285,75,2,2);
   fillellipse(295,75,2,2);
   setcolor(BLACK);/*���*/
   bar(287,80,293,81);
}
void DrawRedflag(int i,int j)/*��ʾ����*/
{
   setcolor(7);
   setfillstyle(SOLID_FILL,RED);
   bar(198+j*20,95+i*20,198+j*20+5,95+i*20+5);
   setcolor(BLACK);
   line(198+j*20,95+i*20,198+j*20,95+i*20+10);
}
void DrawEmpty(int i,int j,int mode,int color)/*���ֿո��ӵ���ʾ*/
{
   setcolor(color);
   setfillstyle(SOLID_FILL,color);
   if(mode==0)/*û�е������Ĵ����*/
      bar(200+j*20-8,100+i*20-8,200+j*20+8,100+i*20+8);
   else
      if(mode==1)/*����������ʾ�հ׵�С����*/
	 bar(200+j*20-7,100+i*20-7,200+j*20+7,100+i*20+7);
}
void GameBegain(void)/*��Ϸ��ʼ����*/
{
   int i,j;
   cleardevice();
   if(gamePLAY!=1)
   {
      MouseSetXY(290,70); /*���һ��ʼ��λ��,����Ϊ���ĳ�ʼ����*/
      MouseX=290;
      MouseY=70;
   }
   gamePLAY=1;/*�´ΰ����¿�ʼ�Ļ���겻���³�ʼ��*/
   mineNUM=0;
   setfillstyle(SOLID_FILL,7);
   bar(190,60,390,290);
   for(i=0;i<10;i++)/*������*/
      for(j=0;j<10;j++)
	 DrawEmpty(i,j,0,8);
   setcolor(7);
   DrawSmile();/*����*/
   randomize();
   for(i=0;i<10;i++)/*100�����������ֵ��û�е���*/
      for(j=0;j<10;j++)
      {
	 Mine[i][j].num=random(8);/*���������Ľ����1��ʾ��������е���*/
	 if(Mine[i][j].num==1)
	    mineNUM++;/*����������1*/
	 else
	    Mine[i][j].num=2;
	 Mine[i][j].flag=0;/*��ʾû�����־*/
      }
   sprintf(randmineNUM,"%d",mineNUM); /*��ʾ����ܹ��ж�������*/
   setcolor(1);
   settextstyle(0,0,2);
   outtextxy(210,70,randmineNUM);
   mineNUM=100-mineNUM;/*����ȡ�հ׸�����*/
   MouseOn();
}
void GameOver(void)/*��Ϸ��������*/
{
   int i,j;
   setcolor(0);
   for(i=0;i<10;i++)
      for(j=0;j<10;j++)
	 if(Mine[i][j].num==1)/*��ʾ���еĵ���*/
	 {
	    DrawEmpty(i,j,0,RED);
	    setfillstyle(SOLID_FILL,BLACK);
	    fillellipse(200+j*20,100+i*20,7,7);
	 }
}
void GameWin(void)/*��ʾʤ��*/
{
   setcolor(11);
   settextstyle(0,0,2);
   outtextxy(230,30,"YOU WIN!");
}
int MineStatistics(int i,int j)/*ͳ��ÿ��������Χ������*/
{
   int nNUM=0;
   if(i==0&&j==0)/*���ϽǸ��ӵ�ͳ��*/
   {
      if(Mine[0][1].num==1)
	 nNUM++;
      if(Mine[1][0].num==1)
	 nNUM++;
      if(Mine[1][1].num==1)
	 nNUM++;
   }
   else
      if(i==0&&j==9)/*���ϽǸ��ӵ�ͳ��*/
      {
	 if(Mine[0][8].num==1)
	    nNUM++;
	 if(Mine[1][9].num==1)
	    nNUM++;
	 if(Mine[1][8].num==1)
	    nNUM++;
      }
     else
	 if(i==9&&j==0)/*���½Ǹ��ӵ�ͳ��*/
	 {
	    if(Mine[8][0].num==1)
	       nNUM++;
	    if(Mine[9][1].num==1)
	       nNUM++;
	    if(Mine[8][1].num==1)
	       nNUM++;
	 }
	else
	    if(i==9&&j==9)/*���½Ǹ��ӵ�ͳ��*/
	    {
	       if(Mine[9][8].num==1)
		  nNUM++;
	       if(Mine[8][9].num==1)
		  nNUM++;
	       if(Mine[8][8].num==1)
		  nNUM++;
	    }
	    else if(j==0)/*��ߵ�һ�и��ӵ�ͳ��*/
	    {
	       if(Mine[i][j+1].num==1)
		  nNUM++;
	       if(Mine[i+1][j].num==1)
		  nNUM++;
	       if(Mine[i-1][j].num==1)
		  nNUM++;
	       if(Mine[i-1][j+1].num==1)
		  nNUM++;
	       if(Mine[i+1][j+1].num==1)
		  nNUM++;
	    }
	    else if(j==9)/*�ұߵ�һ�и��ӵ�ͳ��*/
	    {
	       if(Mine[i][j-1].num==1)
		  nNUM++;
	       if(Mine[i+1][j].num==1)
		  nNUM++;
	       if(Mine[i-1][j].num==1)
		  nNUM++;
	       if(Mine[i-1][j-1].num==1)
		  nNUM++;
	       if(Mine[i+1][j-1].num==1)
		  nNUM++;
	    }
	    else if(i==0)/*��һ�и��ӵ�ͳ��*/
	    {
	       if(Mine[i+1][j].num==1)
		  nNUM++;
	       if(Mine[i][j-1].num==1)
		  nNUM++;
	       if(Mine[i][j+1].num==1)
		  nNUM++;
	       if(Mine[i+1][j-1].num==1)
		  nNUM++;
	       if(Mine[i+1][j+1].num==1)
		  nNUM++;
	     }
	     else if(i==9)/*���һ�и��ӵ�ͳ��*/
	     {
	       if(Mine[i-1][j].num==1)
		  nNUM++;
	       if(Mine[i][j-1].num==1)
		  nNUM++;
	       if(Mine[i][j+1].num==1)
		  nNUM++;
	       if(Mine[i-1][j-1].num==1)
		  nNUM++;
	       if(Mine[i-1][j+1].num==1)
		  nNUM++;
	    }
	    else/*��ͨ���ӵ�ͳ��*/
	    {
	       if(Mine[i-1][j].num==1)
		  nNUM++;
	       if(Mine[i-1][j+1].num==1)
		  nNUM++;
	       if(Mine[i][j+1].num==1)
		  nNUM++;
	       if(Mine[i+1][j+1].num==1)
		  nNUM++;
	       if(Mine[i+1][j].num==1)
		  nNUM++;
	       if(Mine[i+1][j-1].num==1)
		  nNUM++;
	       if(Mine[i][j-1].num==1)
		  nNUM++;
	       if(Mine[i-1][j-1].num==1)
		  nNUM++;
	     }
   return(nNUM);/*�Ѹ�����Χһ���ж���������ͳ�ƽ������*/
}
int ShowWhite(int i,int j)/*��ʾ�������Ŀհײ���*/
{
   if(Mine[i][j].flag==1||Mine[i][j].num==0)/*����к����ø�����Ͳ��Ըø�����κ��ж�*/
      return;
   mineNUM--;/*��ʾ�����ֻ��߿ո�ĸ��Ӿͱ�ʾ�ദ����һ������,�����и��Ӷ�������˱�ʾʤ��*/
   if(Mine[i][j].roundnum==0&&Mine[i][j].num!=1)/*��ʾ�ո�*/
   {
      DrawEmpty(i,j,1,7);
      Mine[i][j].num=0;
   }
   else
      if(Mine[i][j].roundnum!=0)/*�������*/
      {
	 DrawEmpty(i,j,0,8);
	 sprintf(randmineNUM,"%d",Mine[i][j].roundnum);
	 setcolor(RED);
	 outtextxy(195+j*20,95+i*20,randmineNUM);
	 Mine[i][j].num=0;/*�Ѿ���������ĸ�����0��ʾ�Ѿ��ù��������*/
	 return ;
      }
 /*8������ݹ���ʾ���еĿհ׸���*/
   if(i!=0&&Mine[i-1][j].num!=1)
      ShowWhite(i-1,j);
   if(i!=0&&j!=9&&Mine[i-1][j+1].num!=1)
      ShowWhite(i-1,j+1);
   if(j!=9&&Mine[i][j+1].num!=1)
      ShowWhite(i,j+1);
   if(j!=9&&i!=9&&Mine[i+1][j+1].num!=1)
      ShowWhite(i+1,j+1);
   if(i!=9&&Mine[i+1][j].num!=1)
      ShowWhite(i+1,j);
   if(i!=9&&j!=0&&Mine[i+1][j-1].num!=1)
      ShowWhite(i+1,j-1);
   if(j!=0&&Mine[i][j-1].num!=1)
      ShowWhite(i,j-1);
   if(i!=0&&j!=0&&Mine[i-1][j-1].num!=1)
      ShowWhite(i-1,j-1);
}
void GamePlay(void)/*��Ϸ����*/
{
   int i,j,Num;/*Num��������ͳ�ƺ�������һ��������Χ�ж��ٵ���*/
   for(i=0;i<10;i++)
      for(j=0;j<10;j++)
	 Mine[i][j].roundnum=MineStatistics(i,j);/*ͳ��ÿ��������Χ�ж��ٵ���*/
   while(!kbhit())
   {
      if(LeftPress())/*�������̰���*/
      {
	 MouseGetXY();
	 if(MouseX>280&&MouseX<300&&MouseY>65&&MouseY<85)/*������*/
	 {
	    MouseOff();
	    gameAGAIN=1;
	    break;
	 }
	 if(MouseX>190&&MouseX<390&&MouseY>90&&MouseY<290)/*��ǰ���λ���ڸ��ӷ�Χ��*/
	 {
	    j=(MouseX-190)/20;/*x����*/
	    i=(MouseY-90)/20;/*y����*/
	    if(Mine[i][j].flag==1)/*��������к����������Ч*/
	       continue;
	    if(Mine[i][j].num!=0)/*�������û�д����*/
	    {
	       if(Mine[i][j].num==1)/*��갴�µĸ����ǵ���*/
	       {
		  MouseOff();
		  GameOver();/*��Ϸʧ��*/
		  break;
	       }
	       else/*��갴�µĸ��Ӳ��ǵ���*/
	       {
		  MouseOff();
		  Num=MineStatistics(i,j);
		  if(Num==0)/*��Χû���׾��õݹ��㷨����ʾ�հ׸���*/
		     ShowWhite(i,j);
		  else/*���¸�����Χ�е���*/
		  {
		     sprintf(randmineNUM,"%d",Num);/*�����ǰ������Χ������*/
		     setcolor(RED);
		     outtextxy(195+j*20,95+i*20,randmineNUM);
		     mineNUM--;
		  }
	       MouseOn();
	       Mine[i][j].num=0;/*����ĸ�����Χ���������ֱ�Ϊ0��ʾ��������Ѿ��ù�*/
	       if(mineNUM<1)/*ʤ����*/
	       {
		  GameWin();
		  break;
	       }
	    }
	 }
      }
   }
   if(RightPress())/*����Ҽ����̰���*/
   {
      MouseGetXY();
      if(MouseX>190&&MouseX<390&&MouseY>90&&MouseY<290)/*��ǰ���λ���ڸ��ӷ�Χ��*/
      {
	 j=(MouseX-190)/20;/*x����*/
	 i=(MouseY-90)/20;/*y����*/
	 MouseOff();
	 if(Mine[i][j].flag==0&&Mine[i][j].num!=0)/*����û����������ʾ����*/
	 {
	    DrawRedflag(i,j);
	    Mine[i][j].flag=1;
	 }
	 else
	    if(Mine[i][j].flag==1)/*�к����־�ٰ��Ҽ��ͺ�����ʧ*/
	    {
	       DrawEmpty(i,j,0,8);
	       Mine[i][j].flag=0;
	    }
      }
      MouseOn();
      sleep(1);
      }
   }
}


