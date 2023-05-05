# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2022/12/22 14:45
from sqlalchemy import create_engine
from urllib.parse import quote_plus as urlquote
import pandas as pd

from commond.config import setting

zentao_mysql = setting.yaml['zentao']['mysql']


class table_df_factory:
    conn = create_engine(
        f"mysql+pymysql://{zentao_mysql['user']}:{urlquote(zentao_mysql['password'])}@"
        f"{zentao_mysql['host']}:{zentao_mysql['port']}/{zentao_mysql['database']}")

    def product_table_df(self, sql):
        return pd.read_sql(sql, self.conn)

    def product_user(self):
        sql = 'select * from zt_user;'
        return self.product_table_df(sql)

    def product_bug(self):
        sql = 'select * from zt_bug;'
        return self.product_table_df(sql)


zentao_sql = table_df_factory()

if __name__ == '__main__':
    print(table_df_factory().product_user())
