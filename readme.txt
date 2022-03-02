
关于使用manager的问题
不降级则可以尝试修改一下flask_script/__init__.py中from ._compat import text_type 改成
 from flask_script._compat import text_type 。

安装：
pymysql
flask-sqlalchemy
flask-migrate ==2.7.0

步骤
1。配置数据库

2。创建包ext
    __init__.py添加
    db = SQLAlchemy()

    def create_app():
        db.init_app(app)  # 将db对象与app关联

3.migrate:
migrate = Migrate(app=app, db=db)  # 影响数据库映射
manager.add_command('db', MigrateCommand)  # 将命令交给manager管理

4. 创建模型
    model.py
    模型就是类
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(15), nullable=False)
        password = db.Column(db.String(12), nullable=False)
        phone = db.Column(db.String(11), unique=True)
        rdatetime = db.Column(db.DateTime, default=datetime.now)

5.使用命令
    a.在app.py中导入模型
    b.在终端使用命令 db
        python3 app.py db init    ---->产生一个文件夹migrations
        python3 app.py db migrate  ---->产生一个版本文件versions 66c1f07b9ec2_.py

