import pymysql

def find_ip(ip):
    try:
        link = pymysql.Connect(host="127.0.0.1",user="root",password="",database="ip")
        c = link.cursor()
        find_cmd1 = f"SELECT * FROM `ip`.`ip_puls` WHERE minip <= INET_ATON('{ip}') ORDER BY minip DESC LIMIT 1"
        find_cmd = f"SELECT * FROM `ip_puls` WHERE INET_ATON('{ip}') BETWEEN minip AND maxip LIMIT 1"
        c.execute(find_cmd1)
        res = c.fetchall()
        sheng = res[0][7]
        shi = res[0][8]
        xian = res[0][9]
        jing = res[0][12]
        wei = res[0][13]
        wucha = res[0][14]
        print(sheng,shi,xian,jing,wei,wucha)
        c.close()
        link.close()
        return sheng,shi,xian,jing,wei,wucha
    except Exception as err:
        print(err)
        pass
find_ip("39.68.6.78")