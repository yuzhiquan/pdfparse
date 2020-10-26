#!/usr/bin/env python

import pdfplumber
import pandas as pd


def parse(filename):
    with pdfplumber.open(filename) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        # print(text)
        # print(text.split("\n"))
        # for i in text.split("\n"):
        #     for j in i.split(" "):
        #         print(j.encode("utf-8").decode("utf-8"))
        table = page.extract_tables()
        print(table)
        # for t in table:
        #     print(t)
        #     df = pd.DataFrame(t[1:], columns=t[0])
        #     print(df)


if __name__ == '__main__':
    parse("./朱光普个人基本信息.pdf")
