from pymysql import connect

class JD(object):
    def __init__(self):
        # 创建connection连接
        self.conn = connect(host='localhost', port=3306, user='root', password='12345678', database='jing_dong',charset='utf8')
        # 获得cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭cursor对象
        self.cursor.close()
        self.conn.close()

    def show_all_items(self, sql):
        """显示所有的商品"""
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    @staticmethod
    def print_menu():
        print("------京东--------")
        print("1：所有的商品")
        print("2：所有的商品分类")
        print("3：所有的商品品牌分类")
        return input("请输入功能对应的序号：")

    def run(self):
        while True:
            num = self.print_menu()
            if num == '1':
                # 查询所有商品
                sql = "select * from goods;"
                self.show_all_items(sql)
            elif num == '2':
                # 查询分类
                sql = "select * from good_cates;"
                self.show_all_items(sql)
            elif num == '3':
                sql = "select * from goods_brands;"
                self.show_all_items(sql)
            else:
                pass


def main():
    # 1.创建一个京东商城的对象
    jd = JD()

    # 2.调用这个对象的run方法，让其运行
    jd.run()





if __name__ == '__main__':
    main()







