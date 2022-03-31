## 创建
+ mkdir myproject
+ cd myproject
+ python3 -m venv venv
+ . venv/bin/activate （激活虚拟环境）
+ deactivate （停止虚拟环境）

+ pip install Flask

## 启动
+ export FlASK_APP=main
+ export FLASK_ENV=development
+ flask run (本地访问)
+ flask run --host=0.0.0.0 (公开访问)

## 访问
+ http://127.0.0.1:5000/

## flask进程
+ jobs -l  (查看)
+ kill %n (n代表你的flask应用程序编号)