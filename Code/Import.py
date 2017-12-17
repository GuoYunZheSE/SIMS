import xlrd
import pymysql


if __name__ == '__main__':
    xlsx_path=''
    wb=xlrd.open_workbook('xlsx_path')
    sh=wb.sheet_by_index(0)
    dfun=[]
    rows=sh.nrows
    cols=sh.ncols
    fo=[]
    for i in range(1,rows):
        dfun.append(sh.row_values(i))

    conn=pymysql.connect(host='localhost',user='root',passwd='123517',db='')
    cursor=conn.cursor()

    # Create table
    cursor.execute("create table test4(" + fo[0][0] + " varchar(100));")

    #Create table attributes
    for i in range(1,cols):
        cursor.execute("alter table test4 add " + fo[0][i] + " varchar(100);")
    val=''
    for i in range(0,cols):
        var=var+''.format()
    print(dfun)
    cursor.executemany("insert into resources_networkdevice values(" + val[:-1] + ");", dfun)
    conn.commit()