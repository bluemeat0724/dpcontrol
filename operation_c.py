from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# import pytesseract
# from PIL import Image
# from io import BytesIO
# import base64
import re

from sites_info import *


class chrome_operate:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()  # 浏览器属性对象
        self.chrome_options.add_argument('--ignore-ssl-errors=yes')  # 忽略位置网页提示
        self.chrome_options.add_argument(
            '--ignore-certificate-errors')  # 关闭私密链接提示
        self.chrome_options.add_experimental_option('prefs', {'credentials_enable_service': False, 'profile': {
            'password_manager_enabled': False}})  # 不记录密码
        self.chrome_options.add_experimental_option(
            "excludeSwitches", ['enable-automation'])  # 不现实浏览器正在被程序操作
        # self.chrome_options.add_argument(
        #     r"user-data-dir=E:\SynologyDrive\developing_resource\Chrom_user_data");

        self.chrome_options.add_argument("--kiosk")  # 全屏模式
        self.global_loc = 0

        self.page_operations = {'滚动': 'scroll',
                                '顶部': 'top',
                                '下滑': 'down',
                                '上移': 'up',
                                'tab_right':'tab_right',
                                'tab_left':'tab_left'
                                }
        self.url_dict = sites_url_dict

        self.gaoxiao_url = site_gaoxiao_url

        self.challange_url = site_challange_url

        self.peiyu_url = site_peiyu_url
        # self.peiyu_url.update(self.page_operations)

        self.yougu_url = site_yougu_url
        # self.yougu_url.update(self.page_operations)

        self.jzzy_url = site_jzzy_url

        self.quanqiu_url = site_quanqiu_url
        # self.quanqiu_url.update(self.page_operations)

        self.jy_url = site_jy_url
        # self.jy_url.update(self.page_operations)

        self.td_url = site_td_url
        # self.td_url.update(self.page_operations)

        self.cxzs_url = site_cxzs_url
        # self.cxzs_url.update(self.page_operations)

        self.window_handles = []
        self.window_handles_guide = {}


    def web_initialize(self):
        '浏览器初始化'
        try:
            self.driver.current_url
        except:
            self.driver = webdriver.Chrome(
                options=self.chrome_options)  # 打开浏览器
            # self.driver.maximize_window()  # 窗口最大化
        #     open_tabs(driver)
        return self.driver

    def open_new_tab(self, url):
        '打开标签'
        newwindow = 'window.open("{}")'.format(url)
        self.driver.execute_script(newwindow)

    def open_all_tab(self):
        '打开所有页签'
        for i in self.url_dict.keys():
            self.open_new_tab(i)

    def init_handles(self):
        '生成页签导航'
        for i in self.driver.window_handles:
            self.driver.switch_to.window(i)
            i_url = self.driver.current_url
            if i_url == 'data:,' or i_url == 'chrome-search://local-ntp/local-ntp.html':
                self.driver.close()
            else:
                self.window_handles_guide[self.url_dict.get(i_url)] = i
        print(self.window_handles_guide)

    def swich_tabs(self, sitename):
        '切换页签'
        handelcode = self.window_handles_guide[sitename]
        self.driver.switch_to.window(handelcode)

    def switch_tab(self, right=True):
        try:
            handle_index = self.driver.window_handles.index(
                self.driver.current_window_handle)
            handle_num = len(self.driver.window_handles)
            if right:
                handle_index -= 1
            else:
                handle_index += 1
            if 0 < handle_index <= handle_num - 1:
                self.driver.switch_to.window(
                    self.driver.window_handles[handle_index])
            elif handle_index > handle_num - 1:
                handle_index = 0
                self.driver.switch_to.window(
                    self.driver.window_handles[handle_index])
            elif handle_index < -handle_num:
                handle_index = handle_num - 1
                self.driver.switch_to.window(
                    self.driver.window_handles[handle_index])
            else:
                self.driver.switch_to.window(
                    self.driver.window_handles[handle_index])
        except:
            print('tab fail')

    def close_browser(self):
        '关闭浏览器'
        try:
            self.driver.quit()
        except:
            pass

    def close_tab(self):
        '关闭当前页签'
        self.driver.close()

    def refresh(self):  # 刷新
        self.driver.refresh()

    # def read_code(self, img_element):
    #     '读取验证码'
    #     base64_data = re.sub('^data:image/.+;base64,', '',
    #                          img_element.screenshot_as_base64)
    #     byte_data = base64.b64decode(base64_data)
    #     image_data = BytesIO(byte_data)
    #     img = Image.open(image_data)
    #     pytesseract.pytesseract.tesseract_cmd = r'E:\SynologyDrive\工具\Tesseract-OCR\tesseract.exe'
    #     code = pytesseract.image_to_string(img)
    #     return code

    def scroll(self):
        '下滚'
        globalloc = 0
        base = 1 / 20
        for i in range(1, 20):
            height = base * i
            globalloc = height
            script = "window.scrollTo(0,document.body.scrollHeight*{});".format(height)
            self.driver.execute_script(script)
            time.sleep(0.5)

    def scroll_top(self):
        '顶部位置'
        self.global_loc = 0
        script = "window.scrollTo(0,document.body.scrollHeight*{});".format(
            self.global_loc)
        self.driver.execute_script(script)

    def scroll_down(self):
        self.global_loc = self.global_loc + 0.05 if self.global_loc < 1 else 1
        script = "window.scrollTo(0,document.body.scrollHeight*{});".format(
            self.global_loc)
        print(self.global_loc)
        self.driver.execute_script(script)

    def scroll_up(self):
        self.global_loc = self.global_loc - 0.05 if self.global_loc > 0.05 else 0
        script = "window.scrollTo(0,document.body.scrollHeight*{});".format(
            self.global_loc)
        print(self.global_loc)
        self.driver.execute_script(script)

    # 成果库
    def login_check(self):
        '登陆检测，检测是否在登录页面'
        if self.driver.current_url in self.url_dict.keys():
            return False
        else:
            return True

    # 成果库
    def login_chengguo(self):
        '成果库登录'
        self.driver.find_element_by_id(
            "_easyui_textbox_input1").send_keys("system_exhibit")
        self.driver.find_element_by_id(
            "_easyui_textbox_input2").send_keys("System_exhibit123")
        self.driver.find_element_by_link_text('登录').send_keys(Keys.ENTER)

    def chengguo_open(self):
        '打开成果库'
        self.driver.get('http://101.231.72.146:18080/DBZX/login.html')
        # 登录
        if self.login_check() == False:
            print('logging_in')
            self.refresh()
            try:
                self.login_chengguo()
            except:
                pass
        time.sleep(1)

    def check_chengguo(self):
        if self.driver.current_url == 'http://101.231.72.146:18080/DBZX/main.html':
            pass
        else:
            self.chengguo_open()

    def chengguo_main(self):
        '成果主页演示'
        self.check_chengguo()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_link_text('首页').click()
        iframe = self.driver.find_elements_by_xpath(
            './/iframe[contains(@id,"homeStatistics")]')
        self.driver.switch_to.frame(iframe[0])
        # if play:
        #     self.scroll()
        #     self.scroll_top()
        # self.driver.switch_to.default_content()

    def chengguo_openlist(self):
        '打开成果列表'
        self.check_chengguo()
        self.driver.switch_to.default_content()
        try:
            iframe = self.driver.find_elements_by_xpath(
                './/iframe[contains(@id,"fullScientificAchievementMng1")]')
            iframe[0]
            self.driver.find_element_by_link_text('科技成果全库查询').click()
        except:
            iframe = self.driver.find_elements_by_xpath(
                './/iframe[contains(@id,"homeStatistics")]')
            self.driver.switch_to.frame(iframe[0])
            self.driver.find_element_by_id(
                "fullScientificAchievementNum").click()
        self.driver.switch_to.default_content()

    def chengguo_list(self, play=False):
        '操作成果列表'
        self.check_chengguo()
        self.chengguo_openlist()
        iframe = self.driver.find_elements_by_xpath(
            './/iframe[contains(@id,"fullScientificAchievementMng1")]')
        self.driver.switch_to.frame(iframe[0])
        print('转到列表frame')
        if play:
            self.scroll()
            self.scroll_top()

    def chengguo_detail(self):
        '打开成果详情'
        self.check_chengguo()
        try:
            self.driver.find_element_by_link_text('科技成果全库详情').click()
        except:
            self.chengguo_openlist()
            self.chengguo_list(play=False)

            self.driver.find_element_by_id("datagrid-row-r1-2-3").click()
            target = self.driver.find_element_by_id("datagrid-row-r1-2-3")
            ActionChains(self.driver).double_click(target).click().perform()

    def page_operation(self, url_name):
        if url_name == '滚动':
            self.scroll()
        elif url_name == '顶部':
            self.scroll_top()
        elif url_name == '上移':
            self.scroll_up()
        elif url_name == '下滑':
            self.scroll_down()
        elif url_name =='tab_right':
            self.switch_tab()
        elif url_name =='tab_left':
            self.switch_tab(right=False)
        else:
            pass

    def open_gaoxiao(self, url_name):
        if url_name in ['滚动', '顶部', '下滑', '上移']:
            self.page_operation(url_name)
        elif url_name == '体系':
            self.gaoxiao_tixi()
        else:
            self.driver.get(self.gaoxiao_url[url_name])
            self.scroll_top()

    # 高校
    def gaoxiao_tixi(self):
        self.open_gaoxiao('高校主页')
        script = "window.scrollTo(0,document.body.scrollHeight*{});".format(0.6)
        self.driver.execute_script(script)

    # 挑战赛
    def login_challange(self):
        '挑战赛登录'
        print('执行登陆')
        self.driver.find_elements_by_xpath("//input")[0].send_keys("test01")
        self.driver.find_elements_by_xpath("//input")[-1].send_keys("123456")
        self.driver.find_elements_by_xpath("//button")[0].click()

    def challange_open(self):
        self.driver.get('https://challenge.gtechmall.com/passport/login')
        self.login_challange()

    def challange_page(self, url_name):
        if url_name in ['滚动', '顶部', '下滑', '上移']:
            self.page_operation(url_name)
        else:
            self.driver.get(self.challange_url[url_name])
            self.scroll_top()
            if self.driver.current_url.split('?')[0] == 'https://challenge.gtechmall.com/passport/login':
                self.login_challange()
                time.sleep(2)
                self.challange_page(url_name)

    def login_global_fill(self):
        '全球成果登录'
        if self.driver.current_url == 'https://www.t2radar.com/login.jsp':
            self.driver.find_element_by_id(
                "loginname").send_keys("18721070217")
            self.driver.find_element_by_id("password1").send_keys("ABCabc123")
            code_element = self.driver.find_elements_by_id("codeImg")[0]
            code = self.read_code(code_element)
            self.driver.find_element_by_id("code").send_keys(code)
            time.sleep(5)
        else:
            self.driver.get('https://www.t2radar.com/login.jsp')

    def login_global_confirm(self):
        if self.driver.current_url == 'https://www.t2radar.com/login.jsp':
            self.driver.find_element_by_link_text('登陆').click()
        else:
            pass

    def open_webs(self, url_name, urldict):
        if url_name in ['滚动', '顶部', '下滑', '上移']:
            self.page_operation(url_name)
        elif url_name == '体系':
            self.gaoxiao_tixi()
        else:
            self.driver.get(urldict[url_name])
            self.scroll_top()

    def dpclicks(self,commandid):
        '新大屏操作'
        elements=self.driver.find_elements_by_id(commandid)
        for i in elements:
            try:
                i.click()
            except:
                continue




