from flask import render_template,request,redirect,url_for
from web import op
from operation_c import chrome_operate
from flask_wtf  import FlaskForm
from wtforms import SubmitField
import os
import time
from sites_info import dapingdir,dapingbase,ceshidir
from unitcodes import *

co=chrome_operate()

@op.errorhandler(500)
def page_not_found(e):
    return render_template('404.html')

@op.route('/refresh')
def refreshpate():
    co.refresh()
    return 'pagerefreshed'

@op.route('/touch',methods=['GET','POST'])
def main_touch():
    title='系统切换'
    class DynamicForm(FlaskForm):
        pass
    operations=[['万方','search'],['技术交易所','exhibit'],['黄页','yellowpage']]
    setattr(DynamicForm, 'glo', SubmitField('全球成果'))
    setattr(DynamicForm, 'stte', SubmitField('交易所互动'))
    setattr(DynamicForm, 'yellow', SubmitField('黄页'))
    setattr(DynamicForm, 'shanghai', SubmitField('技转动态（上海）'))
    setattr(DynamicForm, 'changsanjiao', SubmitField('技转动态（长三角）'))
    setattr(DynamicForm, 'dpl', SubmitField('技交所大屏（老）'))
    setattr(DynamicForm, 'dpn', SubmitField('技交所大屏'))
    sites = ['https://www.t2radar.com/projectlib/web_index.do', 'D:/12月2日更新html/init.html',
             'http://139.196.114.145:8808/#/enterprise',
             'https://www.t2radar.com/web_bigscreeninter/index.do?id=201912271577418862643',
             'https://www.t2radar.com/web_bigscreeninter/index.do?id=202008211597992472221',
             'http://spstte.stte.com/visiualization/index.html']
    class DynamicForm_b(FlaskForm):
        pass
    setattr(DynamicForm_b, 'login', SubmitField('全球成果登陆'))
    setattr(DynamicForm_b, 'tab_right', SubmitField('切换'))
    form = DynamicForm(request.form)
    form_b= DynamicForm_b(request.form)
    if request.method == 'POST':
        if form_b.tab_right.data:
            co.page_operation('tab_right')
        if form_b.login.data:
            co.driver.get('https://www.t2radar.com/login.jsp')
            co.login_global_fill()
            time.sleep(1)
            co.driver.get(sites[0])
        if form.glo.data:
            co.driver.get(sites[0])
        if form.stte.data:
            co.driver.get(sites[1])
        if form.yellow.data:
            co.driver.get(sites[2])
        if form.shanghai.data:
            co.driver.get(sites[3])
        if form.changsanjiao.data:
            co.driver.get(sites[4])
        if form.dpl.data:
            co.driver.get(sites[5])
        if form.dpn.data:
            return redirect(url_for('web.op_dpn'))
    return render_template('index.html', form=form, form_b=form_b, title=title)


@op.route('/touch_admin',methods=['GET','POST'])
def main_touch_admin():
    title='系统切换'
    class DynamicForm(FlaskForm):
        pass
    operations=[['万方','search'],['技术交易所','exhibit'],['黄页','yellowpage']]
    setattr(DynamicForm, 'glo', SubmitField('全球成果'))
    setattr(DynamicForm, 'stte', SubmitField('交易所互动'))
    setattr(DynamicForm, 'yellow', SubmitField('黄页'))
    setattr(DynamicForm, 'shanghai', SubmitField('技转动态（上海）'))
    setattr(DynamicForm, 'changsanjiao', SubmitField('技转动态（长三角）'))
    setattr(DynamicForm, 'dpl', SubmitField('技交所大屏（老）'))
    setattr(DynamicForm, 'dpn', SubmitField('技交所大屏'))
    sites=['https://www.t2radar.com/projectlib/web_index.do','D:/12月2日更新html/init.html',
           'http://139.196.114.145:8808/#/enterprise',
           'https://www.t2radar.com/web_bigscreeninter/index.do?id=201912271577418862643',
           'https://www.t2radar.com/web_bigscreeninter/index.do?id=202008211597992472221',
           'http://spstte.stte.com/visiualization/index.html']
    class DynamicForm_b(FlaskForm):
        pass
    setattr(DynamicForm_b, 'login', SubmitField('全球成果登陆'))
    setattr(DynamicForm_b, 'tab_right', SubmitField('切换'))
    setattr(DynamicForm_b, 'initop', SubmitField('初始化'))
    setattr(DynamicForm_b, 'close', SubmitField('关闭浏览器'))
    setattr(DynamicForm_b, 'kill', SubmitField('kill&reset'))
    form = DynamicForm(request.form)
    form_b= DynamicForm_b(request.form)
    if request.method == 'POST':
        if form_b.initop.data:
            print('initop')
            co.web_initialize()
        if form_b.kill.data:
            os.system('taskkill /f /im chrome.exe')
            co.web_initialize()
        if form_b.close.data:
            print('initop')
            co.close_browser()
        if form_b.tab_right.data:
            co.page_operation('tab_right')
        if form_b.login.data:
            co.driver.get('https://www.t2radar.com/login.jsp')
            co.login_global_fill()
            time.sleep(1)
            co.driver.get(sites[0])
        if form.glo.data:
            co.driver.get(sites[0])
        if form.stte.data:
            co.driver.get(sites[1])
        if form.yellow.data:
            co.driver.get(sites[2])
        if form.shanghai.data:
            co.driver.get(sites[3])
        if form.changsanjiao.data:
            co.driver.get(sites[4])
        if form.dpl.data:
            co.driver.get(sites[5])
        if form.dpn.data:
            return redirect(url_for('web.op_dpn'))
    return render_template('index.html', form=form, form_b=form_b, title=title)


@op.route('/main_admin',methods=['GET','POST'])
def op_main_admin():
    title='管理员'
    class DynamicForm(FlaskForm):
        pass
    setattr(DynamicForm, 'dpn', SubmitField('技交所大屏'))
    for i, v in co.url_dict.items():
        setattr(DynamicForm, v[1], SubmitField(v[0]))
    class DynamicForm_b(FlaskForm):
        pass
    setattr(DynamicForm_b, 'initop', SubmitField('初始化'))
    setattr(DynamicForm_b, 'dpntest', SubmitField('大屏测试版'))
    setattr(DynamicForm_b, 'close', SubmitField('关闭'))
    setattr(DynamicForm_b, 'kill', SubmitField('kill&reset'))
    form = DynamicForm(request.form)
    form_b= DynamicForm_b(request.form)
    if request.method == 'POST':
        if form_b.initop.data:
            print('initop')
            co.web_initialize()
        if form_b.kill.data:
            os.system('taskkill /f /im chrome.exe')
            co.web_initialize()
        if form_b.close.data:
            print('initop')
            co.close_browser()
        # if form.cgk.data:
        #     return redirect(url_for('web.op_cgk'))
        if form.gx.data:
            return redirect(url_for('web.op_gx'))
        if form.tzs.data:
            return redirect(url_for('web.op_tzs'))
        if form.pyk.data:
            return redirect(url_for('web.op_pyk'))
        if form_b.dpntest.data:
            co.driver.get(ceshidir)
        # if form.jzzy.data:
        #     return redirect(url_for('web.op_jzzy'))
        if form.qq.data:
            return redirect(url_for('web.op_qq'))
        if form.td.data:
            return redirect(url_for('web.op_td'))
        if form.jy.data:
            return redirect(url_for('web.op_jy'))
        if form.cxzs.data:
            return redirect(url_for('web.op_cxzs'))
        if form.dpn.data:
            return redirect(url_for('web.op_dpn'))
        if form.dpn.data:
            return redirect(url_for('web.op_dpn'))
    return render_template('index.html',form=form,form_b=form_b,title=title)

@op.route('/',methods=['GET','POST'])
@op.route('/main',methods=['GET','POST'])
def op_main():
    title='技转工具导航'
    class DynamicForm(FlaskForm):
        pass
    setattr(DynamicForm, 'dpn', SubmitField('技交所大屏'))
    for i, v in co.url_dict.items():
        setattr(DynamicForm, v[1], SubmitField(v[0]))
    class DynamicForm_b(FlaskForm):
        pass
    form = DynamicForm(request.form)
    form_b= DynamicForm_b(request.form)
    if request.method == 'POST':
        print('clickButton')
        # if form.cgk.data:
        #     return redirect(url_for('web.op_cgk'))
        if form.gx.data:
            return redirect(url_for('web.op_gx'))
        if form.tzs.data:
            return redirect(url_for('web.op_tzs'))
        if form.pyk.data:
            return redirect(url_for('web.op_pyk'))
        if form.dp.data:
            co.driver.get('http://spstte.stte.com/visiualization/index.html')
        # if form.jzzy.data:
        #     return redirect(url_for('web.op_jzzy'))
        if form.qq.data:
            return redirect(url_for('web.op_qq'))
        if form.td.data:
            return redirect(url_for('web.op_td'))
        if form.jy.data:
            return redirect(url_for('web.op_jy'))
        if form.cxzs.data:
            return redirect(url_for('web.op_cxzs'))
        if form.dpn.data:
            return redirect(url_for('web.op_dpn'))
    return render_template('index.html',form=form,form_b=form_b,title=title)


@op.route('/cgk,',methods=['GET','POST'])
def op_cgk():
    title = '成果库系统'
    info='科技成果数据库科技成果数据采集，清洗，录入，查询，分析匹配等功能的大数据服务平台。'
    class DynamicForm(FlaskForm):
        pass
    operations=[['打开','open'],['主页','main'],['列表','list'],['详情','detail']]
    for i in operations:
        setattr(DynamicForm, i[1], SubmitField(i[0]))
    class DynamicForm_b(FlaskForm):
        pass
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    setattr(DynamicForm_b, 'tab_right', SubmitField('右tab'))
    setattr(DynamicForm_b, 'tab_left', SubmitField('左tab'))
    form = DynamicForm(request.form)
    form_b = DynamicForm_b(request.form)
    if request.method == 'POST':
        if form.open.data:
            co.chengguo_open()#打开
        if form.main.data:
            co.chengguo_main()
        if form.list.data:
            co.chengguo_openlist()  # 列表
        if form.detail.data:
            co.chengguo_detail()  # 成果详情
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
        for i in ['tab_left','tab_right']:
            if getattr(form_b,i).data:
                co.page_operation(i)
    return render_template('main.html', form=form, form_b=form_b,title=title,info=info)

@op.route('/gx,',methods=['GET','POST'])
def op_gx():
    title = '高校系统'
    info = '汇聚高校技术成果实现高校成果的路演，评估，挂牌，公示，托管等交易前置步骤。为技术交易提供高质量成果。'
    class DynamicForm(FlaskForm):
        pass
    for i in co.gaoxiao_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    for i in co.page_operations.keys():
        setattr(DynamicForm_b, i, SubmitField(i))
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form = DynamicForm(request.form)
    form_b = DynamicForm_b(request.form)
    if request.method == 'POST':
        for i in co.gaoxiao_url.keys():
            if getattr(form,i).data:
                co.open_gaoxiao(i)
        for i in co.page_operations.keys():
            if getattr(form_b,i).data:
                co.page_operation(i)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form, form_b=form_b,title=title,info=info)

@op.route('/tzs,',methods=['GET','POST'])
def op_tzs():
    title = '创新挑战赛'
    info='长三角国际创新挑战赛综合服务平台挖掘技术需求，汇聚技术方案，对接投资意向，激活技术交易市场。'
    class DynamicForm(FlaskForm):
        pass
    # setattr(DynamicForm, 'login_fill', SubmitField('登陆'))
    for i in co.challange_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    for i in co.page_operations.keys():
        setattr(DynamicForm_b, i, SubmitField(i))
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form_b = DynamicForm_b(request.form)
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i in co.challange_url.keys():
            if getattr(form,i).data:
                co.challange_page(i)
        for i in co.page_operations.keys():
            if getattr(form_b,i).data:
                co.page_operation(i)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
        # if form.login_fill.data:
        #     co.challange_open()
        #     time.sleep(1)
    return render_template('main.html', form=form, form_b=form_b,title=title,info=info)

@op.route('/pyk,',methods=['GET','POST'])
def op_pyk():
    title = '科创企业培育库'
    info ='“匠心培育，医话未来”上海市科创企业上市培育库生物医药行业CTO社区'
    class DynamicForm(FlaskForm):
        pass
    for i in co.peiyu_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    for i in co.page_operations.keys():
        setattr(DynamicForm_b, i, SubmitField(i))
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form_b = DynamicForm_b(request.form)
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i in co.peiyu_url.keys():
            if getattr(form,i).data:
                co.open_webs(i,co.peiyu_url)
        for i in co.page_operations.keys():
            if getattr(form_b,i).data:
                co.page_operation(i)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form,form_b=form_b, title=title,info=info)

@op.route('/yg,',methods=['GET','POST'])
def op_yg():
    title = '优股:科技成果权益激励服务平台'
    info = '实现科技项目精选和科技成果权益激励股份交易撮合'
    class DynamicForm(FlaskForm):
        pass
    for i in co.peiyu_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    for i in co.page_operations.keys():
        setattr(DynamicForm_b, i, SubmitField(i))
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form_b = DynamicForm_b(request.form)
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i in co.peiyu_url.keys():
            if getattr(form,i).data:
                co.open_webs(i,co.peiyu_url)
        for i in co.page_operations.keys():
            if getattr(form_b,i).data:
                co.page_operation(i)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form, form_b=form_b,title=title,info=info)

@op.route('/td,',methods=['GET','POST'])
def op_td():
    title = 'TechDeal服务平台'
    info = '聚焦科技成果转化和技术交易领域的咨询门户和互动平台'
    class DynamicForm(FlaskForm):
        pass
    for i in co.td_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    for i in co.page_operations.keys():
        setattr(DynamicForm_b, i, SubmitField(i))
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form_b = DynamicForm_b(request.form)
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i in co.td_url.keys():
            if getattr(form,i).data:
                co.open_webs(i,co.td_url)
        for i in co.page_operations.keys():
            if getattr(form_b,i).data:
                co.page_operation(i)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form, form_b=form_b,title=title,info=info)

@op.route('/dp,',methods=['GET','POST'])
def op_dp():
    title = '交易所大屏(老)'
    class DynamicForm(FlaskForm):
        pass
    setattr(DynamicForm, 'open', SubmitField('打开'))
    setattr(DynamicForm, 'back', SubmitField('返回'))
    form = DynamicForm(request.form)
    if request.method == 'POST':
        if form.open.data:
            co.driver.get('http://spstte.stte.com/visiualization/index.html')
        if form.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form, title=title)

@op.route('/dpn,',methods=['GET','POST'])
def op_dpn():
    title = '交易所大屏'
    buttons = ['成果转化创新中心', '企业联合创新中心', '金融运营创新中心', '区域协同-试点城市','区域协同-合作机构','区域协同-合作意向城市触达','区域协同-海外合作触达', '技术交易服务机构-进场机构']
    pagebuttons = ['科研院所信息服务', '企业信息服务', '产业信息服务', '政府信息服务','技术合同登记']
    buttonids = ['cgzh', 'qylh', 'jsjy', 'sdcs2','hxjy','sdcs', 'hwhz', 'fwjg']
    padecodes = ['institution','enterprise','industry','government','tech_contract']
    class DynamicForm(FlaskForm):
        pass
    setattr(DynamicForm, 'open', SubmitField('打开'))
    for i in range(len(buttons)):
        setattr(DynamicForm, buttonids[i], SubmitField(buttons[i]))
    for i in range(len(pagebuttons)):
        setattr(DynamicForm, padecodes[i], SubmitField(pagebuttons[i]))
    setattr(DynamicForm, 'back', SubmitField('返回'))
    form = DynamicForm(request.form)
    if request.method == 'POST':
        if form.open.data:
            co.driver.get(dapingdir)
        if form.cgzh.data:
            co.dpclicks('cgzh')
        if form.qylh.data:
            co.dpclicks('qylh')
        if form.jsjy.data:
            co.dpclicks('jsjy')
        if form.hxjy.data:
            co.dpclicks('hxjy')
        if form.sdcs2.data:
            co.dpclicks('sdcs2')
        if form.sdcs.data:
            co.dpclicks('sdcs')
        if form.hwhz.data:
            co.dpclicks('hwhz')
        if form.fwjg.data:
            co.dpclicks('fwjg')
        if form.back.data:
            return redirect(url_for('web.op_main'))
        if form.institution.data:
            return redirect(url_for('web.institutions'))
        if form.enterprise.data:
            return redirect(url_for('web.companiesinfo'))
        if form.industry.data:
            co.driver.get(dapingbase+'industryPage.html')
            return redirect(url_for('web.returnpage', title='产业信息服务'))
        if form.government.data:
            return redirect(url_for('web.governmentinfo'))
        if form.tech_contract.data:
            co.driver.get(dapingbase+'govPage2.html')
            return redirect(url_for('web.returnpage',title='技术合同登记'))
    return render_template('main.html', form=form,title=title)

@op.route('/institutions',methods=['GET','POST'])
def institutions():
    title = '科研院所信息服务'
    class DynamicForm(FlaskForm):
        pass
    for i,v in institutioncodes.items():
        setattr(DynamicForm, i, SubmitField(v[1]))
    setattr(DynamicForm, 'back', SubmitField('返回大屏主页'))
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i,v in institutioncodes.items():
            if eval('form.{}.data'.format(i)):
                co.driver.get(dapingbase+'collegePage.html?uid='+str(v[0]))
        if form.back.data:
            co.driver.get(dapingdir)
            return redirect(url_for('web.op_dpn'))
    return render_template('main.html', form=form,title=title)


@op.route('/returnpage',methods=['GET','POST'])
def returnpage():
    title = request.args['title']
    class DynamicForm(FlaskForm):
        pass
    setattr(DynamicForm, 'back', SubmitField('返回大屏主页'))
    form = DynamicForm(request.form)
    if request.method == 'POST':
        if form.back.data:
            co.driver.get(dapingdir)
            return redirect(url_for('web.op_dpn'))
    return render_template('main.html', form=form,title=title)


@op.route('/companiesinfo',methods=['GET','POST'])
def companiesinfo():
    title = '企业信息服务'
    class DynamicForm(FlaskForm):
        pass
    for i,v in enterprisecodes.items():
        setattr(DynamicForm, i, SubmitField(v[1]))
    setattr(DynamicForm, 'back', SubmitField('返回大屏主页'))
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i,v in enterprisecodes.items():
            if eval('form.{}.data'.format(i)):
                co.driver.get(dapingbase+'enterprisePage.html?uid='+str(v[0]))
        if form.back.data:
            co.driver.get(dapingdir)
            return redirect(url_for('web.op_dpn'))
    return render_template('main.html', form=form,title=title)

# @op.route('/industryinfo',methods=['GET','POST'])
# def industryinfo():
#     title = '产业信息服务'

@op.route('/governmentinfo',methods=['GET','POST'])
def governmentinfo():
    title = '政府信息服务'
    class DynamicForm(FlaskForm):
        pass
    for i,v in governmentcodes.items():
        setattr(DynamicForm, i, SubmitField(v[1]))
    setattr(DynamicForm, 'back', SubmitField('返回大屏主页'))
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i,v in governmentcodes.items():
            if eval('form.{}.data'.format(i)):
                co.driver.get(dapingbase+'govPage.html?uid='+str(v[0]))
        if form.back.data:
            co.driver.get(dapingdir)
            return redirect(url_for('web.op_dpn'))
    return render_template('main.html', form=form,title=title)


@op.route('/jzzy,',methods=['GET','POST'])
def op_jzzy():
    title = '技转之眼'
    class DynamicForm(FlaskForm):
        pass
    for i in co.jzzy_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form_b = DynamicForm_b(request.form)
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i in co.jzzy_url.keys():
            if getattr(form, i).data:
                co.open_webs(i, co.jzzy_url)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form,form_b=form_b, title=title)

@op.route('/qq,',methods=['GET','POST'])
def op_qq():
    title = '全球成果'
    info='全球成果汇集，科技成果查询及报告生成'
    class DynamicForm(FlaskForm):
        pass
    setattr(DynamicForm, 'login_fill', SubmitField('登陆'))
    for i in co.quanqiu_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    for i in co.page_operations.keys():
        setattr(DynamicForm_b, i, SubmitField(i))
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form_b = DynamicForm_b(request.form)
    form = DynamicForm(request.form)
    if request.method == 'POST':
        print(os.getcwd())
        for i in co.quanqiu_url.keys():
            if getattr(form, i).data:
                co.open_webs(i, co.quanqiu_url)
        if form.login_fill.data:
            co.driver.get('https://www.t2radar.com/login.jsp')
            co.login_global_fill()
            time.sleep(1)
        for i in co.page_operations.keys():
            if getattr(form_b, i).data:
                co.page_operation(i)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form, title=title,form_b=form_b,info=info)

@op.route('/jy,',methods=['GET','POST'])
def op_jy():
    title = '交易所主页'
    info='实现技术成果转让6大核心流程，受理、发布、登记、签约、结算、凭证。'
    class DynamicForm(FlaskForm):
        pass
    for i in co.jy_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    for i in co.page_operations.keys():
        setattr(DynamicForm_b, i, SubmitField(i))
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form_b = DynamicForm_b(request.form)
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i in co.jy_url.keys():
            if getattr(form,i).data:
                co.open_webs(i,co.jy_url)
        for i in co.page_operations.keys():
            if getattr(form_b, i).data:
                co.page_operation(i)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form,form_b=form_b, title=title,info=info)

@op.route('/cxzs,',methods=['GET','POST'])
def op_cxzs():
    title = '创新助手'
    info = '科技成果查询工具'
    class DynamicForm(FlaskForm):
        pass
    for i in co.cxzs_url.keys():
        setattr(DynamicForm, i, SubmitField(i))
    class DynamicForm_b(FlaskForm):
        pass
    for i in co.page_operations.keys():
        setattr(DynamicForm_b, i, SubmitField(i))
    setattr(DynamicForm_b, 'back', SubmitField('返回'))
    form_b = DynamicForm_b(request.form)
    form = DynamicForm(request.form)
    if request.method == 'POST':
        for i in co.cxzs_url.keys():
            if getattr(form,i).data:
                co.open_webs(i,co.cxzs_url)
        for i in co.page_operations.keys():
            if getattr(form_b, i).data:
                co.page_operation(i)
        if form_b.back.data:
            return redirect(url_for('web.op_main'))
    return render_template('main.html', form=form, title=title,form_b=form_b,info=info)