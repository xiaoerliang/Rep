import sys, os

sys.path.append(os.getcwd()) # /Users/li/Documents/Worker/Rep

from Base.InitDiver import init_driver
from Page.Page import Page_Obj
from Base.Read_Data import ret_yaml_data
import pytest, allure


def read_test_data():
    list_data = []
    test_Data = ret_yaml_data("add_user").get("User")
    for i in test_Data.keys():
        list_data.append((i, test_Data.get(i).get("name")
                          , test_Data.get(i).get("phone"),
                          test_Data.get(i).get("expect")))
    return list_data

class Test_Add_User:
    def setup_class(self):
        self.driver = init_driver()
        self.add_user_obj = Page_Obj(self.driver).return_add_user()

    def teardown_class(self):
        self.driver.quit()
    @allure.step(title="点击新建联系人")
    @pytest.fixture()
    def add_user_btn(self):
        # 添加用户
        self.add_user_obj.click_add()
    @allure.step(title="输入用户信息")
    @pytest.mark.usefixtures("add_user_btn")
    @pytest.mark.parametrize("test_num, name, phone, expect", read_test_data())
    def test_input_user_info(self, test_num, name, phone, expect):

        self.add_user_obj.input_user_info(name, phone)

        if test_num == "test_user_001":
            assert expect not in self.add_user_obj.get_user_list()
        else:
            assert expect in self.add_user_obj.get_user_list()
