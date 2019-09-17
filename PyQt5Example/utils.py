from xml.dom.minidom import parse
import xml.dom.minidom


def config_parse(config_path):
    """
    解析配置文件
    :param config_path:
    """
    res = {'project': 'Unknown',
           'files': []}

    DOMTree = xml.dom.minidom.parse(config_path)
    collection = DOMTree.documentElement

    project_name = collection.getAttribute('name')
    res['project'] = project_name
    testcases_list = collection.getElementsByTagName("testcases")
    for testcases in testcases_list:
        testcases = testcases.getElementsByTagName("testcase")
        for testcase in testcases:
            file_name = testcase.getAttribute('file')
            if testcase.childNodes[0].data == 'Enable':
                res['files'].append(file_name)
    return res
