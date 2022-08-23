from tkinter import *
import json
#导入json头文件
import os,sys
global false, null, true
false = null = true = ''

global inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14




################第一窗口区##################
global app_id_out
root = Tk()
root.geometry('900x650')
root.title('输入你的所有信息')
root.resizable(0,0)


lb1 = Label(root, text='app_id')
lb1.place(relx=0.1, rely=0.05, relwidth=0.2, relheight=0.05)
lb1_ = Label(root, text='例：wx9dfb53543169205')
lb1_.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.05)
inp1 = Entry(root)
inp1.place(relx=0.3, rely=0.05, relwidth=0.2, relheight=0.05)

lb2 = Label(root, text='app_secret')
lb2.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.05)
lb2_ = Label(root, text='例：9c3d7448f44234e32f5b63dec5a5')
lb2_.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.05)
inp2 = Entry(root)
inp2.place(relx=0.3, rely=0.1, relwidth=0.2, relheight=0.05)

lb3 = Label(root, text='template_id')
lb3.place(relx=0.1, rely=0.15, relwidth=0.2, relheight=0.05)
lb3_ = Label(root, text='例：Ewp5WahYUO13ZPJ234TwGKqUQvBlSNXdgcoocS0Q')
lb3_.place(relx=0.55, rely=0.15, relwidth=0.4, relheight=0.05)
inp3 = Entry(root)
inp3.place(relx=0.3, rely=0.15, relwidth=0.2, relheight=0.05)

lb4 = Label(root, text='接受信息的微信号1')
lb4.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.05)
lb4_ = Label(root, text='例：oDzK_6ldDbthJyi342230hB5oEU')
lb4_.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.05)
inp4 = Entry(root)
inp4.place(relx=0.3, rely=0.2, relwidth=0.2, relheight=0.05)

lb5 = Label(root, text='省')
lb5.place(relx=0.1, rely=0.25, relwidth=0.2, relheight=0.05)
lb5_ = Label(root, text='例：湖北')
lb5_.place(relx=0.55, rely=0.25, relwidth=0.4, relheight=0.05)
inp5 = Entry(root)
inp5.place(relx=0.3, rely=0.25, relwidth=0.2, relheight=0.05)

lb6 = Label(root, text='市')
lb6.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.05)
lb6_ = Label(root, text='例：武汉')
lb6_.place(relx=0.55, rely=0.3, relwidth=0.4, relheight=0.05)
inp6 = Entry(root)
inp6.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.05)

lb7 = Label(root, text='对象生日')
lb7.place(relx=0.1, rely=0.35, relwidth=0.2, relheight=0.05)
lb7_ = Label(root, text='例：2001-09-13，如果为农历则写r2001-09-13')
lb7_.place(relx=0.55, rely=0.35, relwidth=0.4, relheight=0.05)
inp7 = Entry(root)
inp7.place(relx=0.3, rely=0.35, relwidth=0.2, relheight=0.05)

lb8= Label(root, text='自己的生日')
lb8.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.05)
lb8_ = Label(root, text='例：2001-09-13，如果为农历则写r2001-09-13')
lb8_.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.05)
inp8 = Entry(root)
inp8.place(relx=0.3, rely=0.4, relwidth=0.2, relheight=0.05)

lb9= Label(root, text='在一起的日子')
lb9.place(relx=0.1, rely=0.45, relwidth=0.2, relheight=0.05)
lb9_ = Label(root, text='例：2001-09-13')
lb9_.place(relx=0.55, rely=0.45, relwidth=0.4, relheight=0.05)
inp9 = Entry(root)
inp9.place(relx=0.3, rely=0.45, relwidth=0.2, relheight=0.05)

lb10= Label(root, text='是否启用词霸每日一句英语')
lb10.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.05)
lb10_ = Label(root, text='是填 True 否填 False，例:False，注意大小写')
lb10_.place(relx=0.55, rely=0.5, relwidth=0.4, relheight=0.05)
inp10 = Entry(root)
inp10.place(relx=0.3, rely=0.5, relwidth=0.2, relheight=0.05)

lb11= Label(root, text='天行APIkey')
lb11.place(relx=0.1, rely=0.55, relwidth=0.2, relheight=0.05)
lb11_ = Label(root, text='例：4f4f6e23423ceb50ff7ea49126cfaf')
lb11_.place(relx=0.55, rely=0.55, relwidth=0.4, relheight=0.05)
inp11 = Entry(root)
inp11.place(relx=0.3, rely=0.55, relwidth=0.2, relheight=0.05)

lb12= Label(root, text='星座')
lb12.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.05)
lb12_ = Label(root, text='例：魔羯座')
lb12_.place(relx=0.55, rely=0.6, relwidth=0.4, relheight=0.05)
inp12 = Entry(root)
inp12.place(relx=0.3, rely=0.6, relwidth=0.2, relheight=0.05)

lb13 = Label(root, text='接受信息的微信号2')
lb13.place(relx=0.1, rely=0.65, relwidth=0.2, relheight=0.05)
lb13_ = Label(root, text='例：oDzK_6qwehJyi342230hB5oEU')
lb13_.place(relx=0.55, rely=0.65, relwidth=0.4, relheight=0.05)
inp13 = Entry(root)
inp13.place(relx=0.3, rely=0.65, relwidth=0.2, relheight=0.05)

################复选框#####################
def win():
    win = Tk()
    win.title("选择你需要调用的API接口")
    win.geometry('800x200')
    win.resizable(0,0)
    lb = Label(text='没有申请的接口请不要勾选，不然会报错',font=('微软雅黑', 10,'bold'),fg='#CD7054')
    lb.pack()
    # 新建整型变量
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    # 设置三个复选框控件，使用variable参数来接收变量
    check1 = Checkbutton(win, text="彩虹屁",font=('微软雅黑', 8,'bold'),variable = CheckVar1,onvalue=1,offvalue=0)
    check2 = Checkbutton(win, text="健康小提示",font=('微软雅黑', 8,'bold'),variable = CheckVar2,onvalue=1,offvalue=0)
    check3 = Checkbutton(win, text="星座运势",font=('微软雅黑', 8,'bold'),variable = CheckVar3,onvalue=1,offvalue=0)
    check4 = Checkbutton(win, text="励志名言",font=('微软雅黑', 8,'bold'),variable = CheckVar4,onvalue=1,offvalue=0)
    check5 = Checkbutton(win, text="下雨建议",font=('微软雅黑', 8,'bold'),variable = CheckVar5,onvalue=1,offvalue=0)
 
    # 选择第一个为默认选项
    # check1.select ()
    check1.pack (side = LEFT)
    check2.pack (side = LEFT)
    check3.pack (side = LEFT)
    check4.pack (side = LEFT)
    check5.pack (side = LEFT)
    # 定义执行函数
    def study():
        global app_id_out,app_secret_out,template_id_out,user_out,province_out,city_out,birthday1_out,birthday2_out,love_date_out,Whether_Eng_out,Whether_caihongpi,astro_out,user2_out,Whether_health,Whether_lucky,Whether_lizhi,Whether_tip
        # 没有选择任何项目的情况下
        if (CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 0 and CheckVar4.get() == 0 and CheckVar5.get() == 0):
            s = '您还没选择任语言'
        else:
            s1 = "彩虹屁" if CheckVar1.get() == 1 else ""
            s2 = "健康小提示" if CheckVar2.get() == 1 else ""
            s3 = "星座运势" if CheckVar3.get() == 1 else ""
            s4 = "励志名言" if CheckVar4.get() == 1 else ""
            s5 = "下雨建议" if CheckVar5.get() == 1 else ""
            s = "您选择了%s %s %s %s %s" % (s1, s2, s3 ,s4, s5)
            #设置标签lb2的字体
            lb2.config(text=s)
            if(CheckVar1.get() == 0):
                Whether_caihongpi=False
            if(CheckVar2.get() == 0):
                Whether_health=False
            if(CheckVar3.get() == 0):
                Whether_lucky=False
            if(CheckVar4.get() == 0):
                Whether_lizhi=False
            if(CheckVar5.get() == 0):
                Whether_tip=False
       


    btn = Button(win,text="选好了",bg='#f9f9f9',command=lambda:[study(),win.destroy()])
    btn.pack(side = LEFT)
    # 该标签，用来显示选择的文本
    lb2 = Label(win,text='',bg ='#f9f9f9',font=('微软雅黑', 11,'bold'),width = 5,height=2)
    lb2.pack(side = BOTTOM, fill = X)
    # 显示窗口

    
    win.mainloop()





# 方法-直接调用 check()
btn1 = Button(root, text='确定', command=lambda:[save(),root.destroy(),win()])
btn1.place(relx=0.4, rely=0.8, relwidth=0.3, relheight=0.05)
def save():
    global app_id_out,app_secret_out,template_id_out,user_out,province_out,city_out,birthday1_out,birthday2_out,love_date_out,Whether_Eng_out,tianxing_API,astro_out,user2_out,Whether_caihongpi,Whether_health,Whether_tip,Whether_lizhi,Whether_lucky
    app_id_out =str(inp1.get())
    app_secret_out =str(inp2.get())
    template_id_out=str(inp3.get())
    user_out=str(inp4.get())
    province_out=str(inp5.get())
    city_out=str(inp6.get())
    birthday1_out=str(inp7.get())
    birthday2_out=str(inp8.get())
    love_date_out=str(inp9.get())
    Whether_Eng_out=inp10.get()
    tianxing_API=str(inp11.get())
    astro_out=str(inp12.get())
    Whether_caihongpi=False
    Whether_health=False
    Whether_tip=False
    Whether_lizhi=False
    Whether_lucky=False
    user2_out=str(inp13.get())

# 在窗体垂直自上而下位置70%处起，布局相对窗体高度40%高的文本框
txt = Text(root)
txt.place(rely=0.9, relheight=0.4)
txt.insert(INSERT,"此项目由二万菌开源提供(小红书账号giddy)\n该项目的Github地址为：https://github.com/erwanjun/weixin_tuisong\n该项目的码云地址为：https://gitee.com/erwanjun/weixin_tuisong")
root.mainloop()



#################写入文件区###################


json_path = 'config.json'
#json原文件

json_path1 = 'config.json'
#修改json文件后保存的路径

dict={}
#用来存储数据

def get_json_data(json_path):
#获取json里面数据

    with open(json_path,'rb') as f:
    #定义为只读模型，并定义名称为f
    
        params = json.load(f)
        #加载json文件中的内容给params
        
        params['app_id'] = app_id_out
        #修改内容
        params['app_secret'] = app_secret_out
        #修改内容
        params['template_id'] = template_id_out
        #修改内容
        params['user'][0] = user_out
        params['user'][1] = user2_out
        #修改内容
        #修改内容
        params['province'] = province_out
        #修改内容
        params['city'] = city_out
        #修改内容
        params['birthday1'] = birthday1_out
        #修改内容
        params['birthday2'] = birthday2_out
        #修改内容
        params['love_date'] = love_date_out
        #修改内容
        params['Whether_Eng'] = Whether_Eng_out
        #修改内容
        params['Whether_caihongpi'] = Whether_caihongpi
        params['Whether_lizhi'] = Whether_lizhi
        params['Whether_tip'] = Whether_tip
        params['Whether_health'] = Whether_health
        params['Whether_lucky'] = Whether_lucky
        params['tianxing_API'] = tianxing_API
        params['astro'] = astro_out

        print("params",params)
        #打印
        
        dict = params
        #将修改后的内容保存在dict中
        
    f.close()
    #关闭json读模式
    
    return dict
    #返回dict字典内容
def write_json_data(dict):
#写入json文件

    with open(json_path1,'w') as r:
    #定义为写模式，名称定义为r
    
        json.dump(dict,r)
        #将dict写入名称为r的文件中
        
    r.close()
    #关闭json写模式

the_revised_dict = get_json_data(json_path)
write_json_data(the_revised_dict)

