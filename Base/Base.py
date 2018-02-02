from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element_o(self,loc, timeout=10, poll=0.5):
        """
        :param loc: 元祖(By.ID,ID属性值)
        :param timeout:
        :param poll:
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_element(*loc))
    def find_elements_o(self,loc, timeout=10, poll=0.5):
        """
        :param loc: 元祖(By.ID,ID属性值)
        :param timeout:
        :param poll:
        :return: 一组定位对象
        """
        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_elements(*loc))

    def if_disp(self,loc):
        # 判断元素是否存在
        try:
            self.find_element_o(loc)
            return True
        except Exception as e:
            return False

    def click_element(self, loc):
        # 点击函数
        self.find_element_o(loc).click()

    def input_text(self, loc, text):
        """
        :param loc:
        :param text: 输入的内容
        :return:
        """
        ele = self.find_element_o(loc)
        ele.clear()
        ele.send_keys(text)

