# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2021/12/17 13:46
import os.path

# 忽略警告
import urllib3
from exchangelib import Account, Message, Mailbox, Credentials, DELEGATE, Configuration, NTLM, BaseProtocol, \
    NoVerifyHTTPAdapter, Version, Build, FileAttachment

from commond.config import setting

urllib3.disable_warnings()

# 忽略SSL认证
# BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

# 配置exchange的版本
# https://exchange.kbd.com/owa 查看版本
version = Version(build=Build(8, 0))
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter


class MyEmail:

    def __init__(self):
        data = setting.yaml['email']['send_email']
        self.account = None
        self.create_account(**data)

    def create_account(self, username, password, server='exchange.kbd.com', name='陈亮亮'):
        """
        登录账户值服务器！
        :return: account
        """
        credentials = Credentials(username=username, password=password)
        # config = Configuration(server=server, credentials=credentials, auth_type=NTLM, version=version)
        config = Configuration(server=server, credentials=credentials, auth_type=NTLM,
                               version=Version(build=Build(8, 0)))
        self.account = Account(
            primary_smtp_address='%s@heading.loc' % username.split(os.sep)[-1],
            fullname=name,
            config=config,
            credentials=credentials,
            autodiscover=False,
            access_type=DELEGATE,
        )

    def send_message(self, subject, body, file_path, to_recipients, cc_recipients):
        """
        发送邮件
        :param subject: 主题
        :param body: 正文
        :param file_path: 附件路径_list
        :param to_recipients: 收件人列表 ---> list
        :param cc_recipients: 抄送人列表 ---> list
        :param pcc_recipients: 秘送人列表 ---> list
        :return:
        """
        to_recipients = [Mailbox(email_address=i) for i in to_recipients]
        cc_recipients = [Mailbox(email_address=i) for i in cc_recipients]
        m = Message(account=self.account, subject=subject, body=body,
                    to_recipients=to_recipients, cc_recipients=cc_recipients, folder=self.account.sent)
        for file in file_path:
            if os.path.isfile(file):
                with open(file, 'rb') as f:
                    cont = f.read()
                my_file = FileAttachment(name=file.split(os.sep)[-1], content=cont)
                m.attach(my_file)
        m.send_and_save()


my_email = MyEmail()

if __name__ == '__main__':
    # print(setting.path.config_path + os.sep + 'email.yaml')
    # email = MyEmail()
    my_email.send_message('测试发送附件ce', '测试发送附件111',
                          file_path=[r"F:\git\zentao_tools\Result\全部bug统计.xlsx"],
                          to_recipients=['zuheg@heading.loc'], cc_recipients=[])
