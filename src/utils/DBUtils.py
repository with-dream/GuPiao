import pymysql


class DBUtils(object):
    db = pymysql.connect(host='localhost', port=3306, db='gupiao', user='root', password='123456')
    cursor = db.cursor()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(DBUtils, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

    def init(self):
        sqlDB = """
            CREATE DATABASE IF NOT EXISTS gupiao
            DEFAULT CHARACTER SET utf8
            DEFAULT COLLATE utf8_general_ci;
        """
        self.cursor.execute(sqlDB)
        sqlTB = """
            CREATE TABLE IF NOT EXISTS `code_map`(
               `id` INT UNSIGNED AUTO_INCREMENT,
               `code` INT(6) NOT NULL,
               `name` VARCHAR(50) NOT NULL,
               PRIMARY KEY ( `id` )
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
        self.cursor.execute(sqlTB)