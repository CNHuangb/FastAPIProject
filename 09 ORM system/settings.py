TORTOISE_ORM = {


    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # 使用MySQL引擎
            "credentials": {
                "host": "172.16.2.219",  # 数据库地址
                "port": 3306,  # 数据库端口
                "user": "root",  # 数据库用户名
                "password": "bmc.123",  # 数据库密码
                "database": "fastapi_orm",  # 数据库名称
                "charset": "utf8mb4",  # 字符编码
                "minsize": 1,  # 连接池最小连接数
                "maxsize": 10,  # 连接池最大连接数
                "echo": True  # 打印SQL语句
            }
        }
    },
    "apps": {
        "models": {
            "models": ["models","aerich.models"],  # 注册模型文件夹名.文件名，从项目根目录开始写
            "default_connection": "default"  # 默认数据库连接
        }
    },
    "use_tz": False,  # 关闭时区处理
    "timezone": "Asia/Shanghai"  # 设置时区为上海




}