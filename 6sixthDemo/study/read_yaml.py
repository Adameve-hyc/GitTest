'''
读取yaml文件
语法：yaml.safe_laod(待读取文件对象)
注意：读取文件时，为防止出现编码错误需要encoding='utf-8'
返回数据：字典形式
'''
import yaml

class get_data():

    def get_yml_data(self):
        with open("./write_yaml.yml",'r',encoding='utf-8') as f:
            value = yaml.safe_load(f)
            print(value)
            print(type(value))




if __name__ == '__main__':
    get_data().get_yml_data()



