
关于使用manager的问题
不降级则可以尝试修改一下flask_script/__init__.py中from ._compat import text_type 改成
 from flask_script._compat import text_type 。

安装：
pymysql
flask-sqlalchemy
flask-migrate
