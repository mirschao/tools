# coding: utf-8
# @author: liuchao
# @email: mirs_chao@163.com
# @github: https://github.com/mirschao
# @usage: insert data into mysql databases's table


import pymysql.cursors
from faker import Faker


class InsertData():
    def __init__(self) -> None:
        self.dbhost = "172.16.12.11"
        self.dbport = 3306
        self.dbuser = "test"
        self.dbpasswd = "Qfcloud120.."

    
    def insert(self):
        connection = pymysql.connect(
            host=self.dbhost,
            port=self.dbport,
            user=self.dbuser,
            password=self.dbpasswd,
            database="qfcloud",
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection:
            with connection.cursor() as cursors:
                generator = Faker()
                for _ in range(10000):
                    username, address, email, password = generator.user_name(), generator.address(), generator.company_email(), generator.password()
                    sql = f"INSERT INTO `userlist` (`username`, `address`, `email`, `password`) VALUES ('{username}', '{address}', '{email}', '{password}')"
                    cursors.execute(sql)
                    print(f"username: {username} add complete!")
            connection.commit()


if __name__ == '__main__':
    insert = InsertData()
    insert.insert()
