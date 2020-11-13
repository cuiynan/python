import pymysql


def mysql(host, userName, passWord, dbName, sql):
    # 打开数据库连接
    import pymysql

    # 建立数据库连接
    conn = pymysql.connect(
        host=host,
        port=3306,
        user=userName,
        password=passWord,
        db=dbName,
        charset='utf8'
    )
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()
    # print("Database version : %s " % data)
    # 关闭数据库连接
    conn.close()
    return data


def selectOne(host, userName, passWord, dbName, sql):
    # 打开数据库连接
    import pymysql

    # 建立数据库连接
    conn = pymysql.connect(
        host=host,
        port=3306,
        user=userName,
        password=passWord,
        db=dbName,
        charset='utf8'
    )
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()
    # print("Database version : %s " % data)
    # 关闭数据库连接
    conn.close()
    return data