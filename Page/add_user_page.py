from Base.Base import Base
import Page, time, allure

class Add_User_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_add(self):
        # 点击添加用户按钮
        self.click_element(Page.add_user)

    def click_save_local(self):
        # 点击本地保存
        self.click_element(Page.save_local)
    def get_user_list(self):
        # 获取联系人列表
        user_data = self.find_elements_o(Page.user_text)
        return [i.text for i in user_data]

    def input_user_info(self, name, phone):
        # 输入用户名
        allure.attach("描述", "输入用户名")
        self.input_text(Page.send_name, name)
        # 电话 点击返回保存
        allure.attach("描述", "输入手机号")
        self.input_text(Page.send_phone, phone)
        # 点击返回保存
        allure.attach("描述", "点击添加页返回按钮")
        self.click_element(Page.click_save_back)
        # 判断是否在用户详情页
        if self.if_disp(Page.usr_edit_btn):
            allure.attach("描述", "点击手机返回按钮")
            self.driver.keyevent(4)