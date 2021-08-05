import yaml


class Utils:

    @classmethod
    def get_yaml_data(cls, file_path):
        """
          封装yaml 文件的读取方法
        :param file_path: yaml 文件的路径
        :return: 字典格式的yaml 文件内容
        """
        with open(file_path) as f:
            datas = yaml.safe_load(f)
        return datas
