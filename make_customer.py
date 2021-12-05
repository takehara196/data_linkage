# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import datetime

d_today = datetime.date.today()

def _make_customer_data():
    # レコード数の指定
    record_count = 5000

    customer_cols_csv = [
        "顧客コード",
        "顧客名",
        "顧客名カナ",
        "郵便番号",
        "都道府県",
        "市区町村",
        "番地",
        "建物",
        "電話番号",
        "FAX番号",
        "法人番号",
        "代表者",
        "設立年月日",
        "決算月",
        "売上高",
        "従業員数",
        "削除フラグ"
    ]

    df = pd.DataFrame(
        index=range(record_count),
        columns=customer_cols_csv
    )

    customer_code_list = []
    customer_name_list = []
    for num in range(record_count):
        customer_code_list.append(f"customer_code_{str(num + 1).zfill(len(str(record_count)))}")
        customer_name_list.append(f"customer_name_{str(num + 1).zfill(len(str(record_count)))}")

    customer_code_df = pd.DataFrame(customer_code_list)
    customer_name_df = pd.DataFrame(customer_name_list)
    df['顧客コード'] = customer_code_df
    df['顧客名'] = customer_name_df
    df['削除フラグ'] = 0

    df.to_csv(f"input_data/customer_{d_today}.csv", index=False)

    return customer_code_df


def _make_contract_data(customer_code_df):
    # レコード数の指定
    record_count = 5000

    contract_cols_csv = [
        "契約コード",
        "顧客コード",
        "契約名",
        "契約名カナ",
        "契約区分",
        "フェーズ",
        "担当",
        "契約開始日",
        "契約終了日",
        "契約終了予定日",
        "削除フラグ"
    ]

    df = pd.DataFrame(
        index=range(record_count),
        columns=contract_cols_csv
    )

    contract_code_list = []
    contract_name_list = []
    for num in range(record_count):
        contract_code_list.append(f"contract_code_{str(num + 1).zfill(len(str(record_count)))}")
        contract_name_list.append(f"contract_name_{str(num + 1).zfill(len(str(record_count)))}")

    contract_code_df = pd.DataFrame(contract_code_list)
    contract_name_df = pd.DataFrame(contract_name_list)
    df['契約コード'] = contract_code_df
    df['顧客コード'] = customer_code_df
    df['契約名'] = contract_name_df
    df['削除フラグ'] = 0

    df.to_csv(f"input_data/contract_{d_today}.csv", index=False)

    return contract_code_df


def _make_custom_variable(contract_code_df):
    # データ作成開始年月日
    start_date = "2021/10/01"
    # データ作成終了年月日
    end_date = "2021/12/01"

    # レコード数の指定
    record_count = 5000

    # カスタム変数のカラム数
    custom_variable_count = 20

    custom_variable_list = []
    for c in range(custom_variable_count):
        custom_variable_list.append(f"変数{c + 1}")

    custom_variable_list.insert(0, "年月日")
    custom_variable_list.insert(1, "契約コード")
    custom_variable_list.append("削除フラグ")

    df = pd.DataFrame(
        (np.random.randn(record_count, len(custom_variable_list))*100).round(),
        index=range(record_count),
        columns=custom_variable_list
    )

    df['年月日'] = start_date
    df['契約コード'] = contract_code_df
    df['削除フラグ'] = 0

    df.to_csv(f"input_data/custom_variable_{d_today}.csv", index=False)

    return


def main():
    customer_code_df = _make_customer_data()
    contract_code_df = _make_contract_data(customer_code_df)
    _make_custom_variable(contract_code_df)


if __name__ == '__main__':
    main()
