import pymysql


def get_conn():

    conn = pymysql.connect(user='team', host='122.112.231.109', port=3306, password='123456', database='myhealth', charset='utf8')
    return conn


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
            conn.commit()
            return items1,items2
        except:
            conn.rollback()
            return [],[]
        finally:
            conn.close()
            cursor1.close()

def show_tables():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("show tables;")
        items = cursor.fetchall()
        conn.commit()
        return items
    except:
        conn.rollback()
        return []
    finally:
        conn.close()
        cursor.close()


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


