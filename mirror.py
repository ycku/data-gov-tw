# 0:id
# 1:資料集名稱
# 2:服務分類
# 3:檔案格式
# 4:下載連結
# 5:編碼格式
# 6:資料類型
# 7:資料集描述
# 8:主要欄位說明
# 9:提供機關
# 10:更新頻率
# 11:授權方式
# 12:授權說明網址
# 13:計費方式
# 14:資料集提供機關聯絡人
# 15:資料集提供機關聯絡人電話
# 16:發布時間
# 17:修訂時間
# 18:備註

import os
import csv
import requests

CSV_URL = 'https://data.gov.tw/dataset/export/csv'
DATA_PATH = 'data/'
if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row[0])
        DIR_PATH = DATA_PATH + row[0]
        if not os.path.exists(DIR_PATH):
            os.makedirs(DIR_PATH)
        type = row[3].split(';')
        url = row[4].split(';')
        for i in range(len(type)):
            if (type[i] == 'CSV' or type[i] == 'JSON' or type[i] == 'XML') and i < len(url):
                print(type[i] + ':' + url[i])


