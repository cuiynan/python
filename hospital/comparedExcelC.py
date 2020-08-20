import xlrd

from hospital.Hospitals import Hospital


# 加载全部爬下来的医院


def loadCommonExcel(hospitalALL, path, code, name, addr, kind):
    data = xlrd.open_workbook(path)
    print(data.sheet_names())
    table = data.sheet_by_name(data.sheet_names()[0])
    row = table.nrows
    for i in range(row):
        hospital = Hospital()
        if (code != -1):
            hospital.code = table.cell(i, code).value
        hospital.name = table.cell(i, name).value.strip()
        if (addr != -1):
            hospital.address = table.cell(i, addr).value.strip()
        hospital.type = '医院'
        if (kind != -1):
            hospital.kind = table.cell(i, kind).value.strip()
        hospitalALL.append(hospital)

def doWork(html):
    soup = BeautifulSoup(html, 'html.parser')
    hospital = Hospital()
    hospital.code = soup.select('title')[0].text.replace('_百度搜索','')
    try:
        hospital.name = soup.select('h3 a em')[0].text
        hospital.address = soup.select('.op-map-singlepoint-info-right')[0].contents[0]
        hospital.print
    except:
        hospital.print