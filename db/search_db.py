import pymysql


# 连接数据库
def get_conn():
    conn = pymysql.connect(user='team', host='122.112.231.109', port=3306, password='123456', database='myhealth', charset='utf8')
    return conn


# 查询表
def search_table(table):
        conn = get_conn()
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        try:
            sql1 = "select * from {};".format(table)
            sql2 = "desc {}".format(table)
            cursor1.execute(sql1)
            cursor2.execute(sql2)

            items1 = cursor1.fetchall()
            items2 = cursor2.fetchall()
            print(items2)
            conn.commit()
            return items1,items2
        except Exception as e:
            print(e)
            conn.rollback()
            return [],[]
        finally:
            conn.close()
            cursor1.close()


# 显示表
def show_tables():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("select english,chinese from translate;")
        items = cursor.fetchall()
        conn.commit()
        return items
    except:
        conn.rollback()
        return []
    finally:
        conn.close()
        cursor.close()


# 组装表数据
def package_items(items1,items2):
    items_list = []
    for i in range(len(items1)):
        sub_list = []

        for j in range(len(items2)):
            if items1[i][j] == None:
                sub_list.append([items2[j][0], ""])
            else:
                sub_list.append([items2[j][0], items1[i][j]])
        items_list.append(sub_list)
    return items_list


# 添加字段
def insert_field(sql):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
    finally:
        conn.close()
        cursor.close()


# 组装添加sql
def insert_sql(value_dict,table):
    k_list = []
    v_list = []
    for k, v in value_dict.items():
        k_list.append(k)
        v_list.append(v)
    k_str = ",".join(k_list)
    v_str = ""
    for v_s in v_list:
        if type(v_s) == str:
            v_str += "'"+v_s+"'"
            v_str += ","
        else:
            v_str += str(v_s)
            v_str += ","
    v_str1 = v_str[:-1]
    sql = "insert into {}({}) values({});".format(table, k_str, v_str1)
    return sql


# 组装更新sql
def update_sql(value_dict,table):
    k_list = []
    v_list = []
    for k, v in value_dict.items():
        k_list.append(k)
        v_list.append(v)
    str_ups = ""
    str_v = ""
    for i in range(len(k_list)):
        if i == 0:
            str_id = k_list[i]
            str_val = v_list[i]
            str_v = str_id +"="+str_val
        else:
            str_up = k_list[i] + "='"+v_list[i]+"'"
            str_ups += str_up + ","
    str_update = str_ups[:-1]
    sql = "update {} set {} where {};".format(table,  str_update, str_v)
    return sql


# 表字段查询
def desc_table(table):
    conn = get_conn()
    cursor = conn.cursor()
    sql = "desc {}".format(table)
    try:
        cursor.execute(sql)
        item = cursor.fetchall()
        conn.commit()
        return item
    except:
        conn.rollback()
        return []
    finally:
        conn.close()
        cursor.close()


# 组装模糊查询sql
def search_str(str,table):
    item = desc_table(table)
    conn = get_conn()
    cursor = conn.cursor()
    str_sql = ""
    for table_name in item:
        str_sql += table_name[0]+" "+"like '%"+str+ "%' or "
    sqlstr= str_sql[:-3]
    sql = "select * from {} where {};".format(table, sqlstr)
    print(sql)
    try:
        cursor.execute(sql)
        item = cursor.fetchall()
        conn.commit()
        return item
    except:
        conn.rollback()
        return []
    finally:
        conn.close()
        cursor.close()


# 获取表名
def get_tname(table):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("select chinese from translate where english='{}';".format(table))
        items = cursor.fetchall()
        conn.commit()
        return items[0][0]
    except:
        conn.rollback()
        return []
    finally:
        conn.close()
        cursor.close()




