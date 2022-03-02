from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps import create_app
from exts import db

from apps.user.model import User

app = create_app()

manager = Manager(app=app)

# 命令工具
migrate = Migrate(app=app, db=db)  # 影响数据库映射
manager.add_command('db', MigrateCommand)  # 将命令交给manager管理


@manager.command
def init():
    print('初始化')


if __name__ == '__main__':
    manager.run()
