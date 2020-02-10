import os
import yaml



def read_yaml():
    base_path = os.path.dirname(os.path.abspath(__file__))
    with open(base_path+os.sep+'sum_data.yaml','r',encoding='utf-8') as f:
        data = yaml.safe_load(f).values()
        data_list = list()
        for i in data:
            da = i.values()
            for n in da:
                data_list.append((n.get('a'),
                                  n.get('b'),
                                  n.get('c')))

        return data_list


read_yaml()