'''
编写yaml
方式一：直接编写
        见write_yaml.yml文件
方式二：代码写入
语法：yaml.safe_dump('字典类型数据'，'待写入文件流(f)',encoding='utf-8',allow_unicode=True)
注意：传入必须写encoding='utf-8',allow_unicode=True
    encoding='utf-8'   指定使用utf-8编码
    allow_unicode=True      使用unicode编码
'''
import yaml
import os

data = {'Search_Data': {
 'search_test_002': {'expect': {'value': '你好'}, 'value': '你 好'},
 'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

base_path = os.path.dirname(os.path.abspath(__file__))

with open(base_path+os.sep+'03_python_write_yaml.yml','a',encoding='utf-8') as f:
    yaml.safe_dump(data,f,encoding='utf-8',allow_unicode=True)

print(base_path+os.sep+'03_python_write_yaml.yml')