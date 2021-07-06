#chromdriver:http://npm.taobao.org/mirrors/chromedriver/
import os


sites_url_dict = {
    # 'http://spstte.stte.com/visiualization/index.html': ['技交所大屏(老)', 'dp'],
    # 'https://101.231.72.132:8080/DBZX/html/bigScreen20200410/index.html#/': ['技转之眼', 'jzzy'],
    # 'http://101.231.72.146:18080/DBZX/login.html': ['成果库', 'cgk'],
                 # 'http://101.37.157.9:8104/home': ['余杭项目审核(孵化)','fh'],
                 'https://www.gaoxiaotech.com/index.html': ['高校技术市场平台(高校)', 'gx'],
                 'https://challenge.gtechmall.com/passport/login': ['挑战赛（需求）', 'tzs'],
                 # 'http://www.peiyuku.com/': ['培育库（企业）', 'pyk'],
                 # 'http://101.37.157.9:8080/home': ['优股（撮合）','yg'],
                 # 'https://www.t2radar.com/login.jsp': ['全球成果（数据）', 'qq'],
                 'https://www.techdeal.cn': ['TechDeal（服务）', 'td'],
                 'http://www.stte.com/': ['交易所主页（交易）', 'jy'],
                 # 'http://www.kjzjfw.com/Index': ['一券通：创新券（政策）', 'cxq'],
                 # 'https://www.gtechmall.com/': ['技术商城', 'sc'],
                 # 'https://webstads.sciinfo.cn/stads.do?index': ['创新助手', 'cxzs']

                 }

site_gaoxiao_url = {'高校主页': 'https://www.gaoxiaotech.com/index.html',
                    '直通车': 'https://www.gaoxiaotech.com/cgztc_index.html',
                    '评估(评估列表)': 'https://www.gaoxiaotech.com/index_assessment_list.html',
                    '评估（我要评估）':'https://www.gaoxiaotech.com/index_assessment.html',
                    '挂牌': 'https://www.gaoxiaotech.com/index_listing_list.html',
                    '公示': 'https://www.gaoxiaotech.com/index_list.html',
                    '托管': 'https://www.gaoxiaotech.com/index_trusteeship_list.html',
                    '关于我们': 'https://www.gaoxiaotech.com/index_about.html',
                    '体系': 'https://www.gaoxiaotech.com/index.html',
                    }


site_challange_url = {'主页': 'https://challenge.gtechmall.com/index',
                      '疫情专区': 'https://challenge.gtechmall.com/subIndex?challenge=45',
                      # '发布需求': 'https://challenge.gtechmall.com/demand',
                      '需求列表': 'https://challenge.gtechmall.com/case',
                      '需求详情': 'https://challenge.gtechmall.com/case/11033',
                      '匹配报告1': os.path.join(os.getcwd(),'static','report_page1.png'),
                      '匹配报告2': os.path.join(os.getcwd(),'static','report_page_menu.png'),
                      '匹配报告3': os.path.join(os.getcwd(),'static','report_page_match.png'),
                      '大赛新闻': 'https://challenge.gtechmall.com/news/list',
                      '通知公告': 'https://challenge.gtechmall.com/news/notice/list',
                      '活动大厅': 'https://challenge.gtechmall.com/active',
                      }
dapingdir='http://139.196.114.145:8000/index/index.html?distort=true'
dapingbase='http://139.196.114.145:8000/'

ceshidir="http://139.196.114.145:9909/index/index.html?distort=true"
ceshibase='http://139.196.114.145:9909/'

# dapingdir='E:/SynologyDrive/python/pycharm/dp/visiualizationpage/index/index.html'
# dapingbase='E:/SynologyDrive/python/pycharm/dp/visiualizationpage/'

site_peiyu_url = {'主页': 'http://www.peiyuku.com/site/index',
                  '企业库': 'http://www.peiyuku.com/corp/index',
                  '服务商': 'http://www.peiyuku.com/provider/index',
                  '专家库': 'http://www.peiyuku.com/expert/index',
                  '服务产品（培育方案）': 'http://www.peiyuku.com/solution/index',
                  '培育指南（培育方案）': 'http://www.peiyuku.com/corp/pyzn',
                  '服务案例（培育方案）': 'http://www.peiyuku.com/solution/service',
                  }

site_yougu_url = {'主页': 'http://101.37.157.9:8080/home',
                  '权益记录股份交易撮合': 'http://101.37.157.9:8080/finance',
                  '科技成果交易撮合': 'http://101.37.157.9:8080/technology',
                  '企业权益激励定制化服务': ''
                  }

site_jzzy_url = {'主页': 'https://101.231.72.132:8080/DBZX/html/bigScreen20200410/index.html#/',
                 '企业主体': 'https://101.231.72.132:8080/DBZX/html/bigScreen20200410/index.html#/enterprise',
                 '交易': 'https://101.231.72.132:8080/DBZX/html/bigScreen20200410/index.html#/transactions',
                 '技术输出': 'https://101.231.72.132:8080/DBZX/html/bigScreen20200410/index.html#/flows',
                 '成果策源': 'https://101.231.72.132:8080/DBZX/html/bigScreen20200410/index.html#/achievements',
                 '服务载体': 'https://101.231.72.132:8080/DBZX/html/bigScreen20200410/index.html#/services'
                 }

site_quanqiu_url = {
                    # '登陆页':'https://www.t2radar.com/login.jsp',
                    '全球项目库':'https://www.t2radar.com/projectlib/web_index.do',
                    '项目详情案例':'https://www.t2radar.com/projectlib/web_toDetal.do?id=2019-03128&path=',
                    '报告系统':'https://www.t2radar.com/web_tem/goReport.do',
                    '报告样例':os.path.join(os.getcwd(),'static','report_sample.pdf')}

# 'https://tdpc.ytangdata.com/transaction/search': ['TechDeal（服务）', 'td'],
site_td_url={'主页':'https://www.techdeal.cn',
             '交易（成果）':'https://www.techdeal.cn/transaction/achievement',
             '交易（需求）':'https://www.techdeal.cn/demand',
             '交易（融资)':'https://www.techdeal.cn/transaction/financing',
             '活动':'https://www.techdeal.cn/activity',
             '资讯':'https://www.techdeal.cn/news',
             '圈子':'https://www.techdeal.cn/circle',
             'APP下载':'https://www.techdeal.cn/app-download',
             }

# 'http://www.stte.com/': ['交易所主页（交易）', 'jy'],
site_jy_url={
    '主页':'http://www.stte.com/',
    '交易':'http://www.stte.com/transactions',
    '服务介绍':'http://www.stte.com/services',
    '服务介绍（企业)':'http://www.stte.com/services/business',
    '服务介绍（科研机构）':'http://www.stte.com/services/scientific-research',
    '服务介绍（区域）':'http://www.stte.com/services/gov',
    '竞价系统':'http://www.stte.com/bidding',
    '要闻':'http://www.stte.com/events',
    '简介':'http://www.stte.com/about'
}

# 'http://www.kjzjfw.com/Index': ['一券通：创新券（政策）', 'cxq'],


# 'https://www.gtechmall.com/': ['技术商城', 'sc'],
# site_sc_url = {'主页':'https://www.gtechmall.com/'}

# 'https://webstads.sciinfo.cn/stads.do?index': ['创新助手', 'cxzs']
site_cxzs_url = {'主页':'https://webstads.sciinfo.cn/stads.do?index'}
