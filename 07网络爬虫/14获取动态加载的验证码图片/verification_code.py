# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/5/10  14:53
# 文件名称   ：verification_code.py
# 开发工具   ：PyCharm
import datetime

from selenium import webdriver  # 导入浏览器驱动模块

# 设置chrome为无界面浏览器
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')

# 打开浏览器
driver = webdriver.Firefox(options=options)
# 加载谷歌浏览器驱动
# driver = webdriver.Firefox()
# 浏览器窗口全屏显示
# driver.maximize_window()
# 发送网络请求，实现浏览器打开页面
driver.get('http://my.cnki.net/elibregister/commonRegister.aspx')

# 获取网页中验证码html代码标签
dynamic = driver.find_element_by_class_name('dynamic-pic')
# print(dynamic)
print(str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
dynamic.screenshot('F:/' + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + 'code.png')  # 对验证码进行截屏,并保存在指定目录下
driver.close()    # 关闭浏览器窗口