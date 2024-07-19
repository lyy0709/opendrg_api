# 使用官方的 Python 基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录
COPY . /app

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 服务运行的端口
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=api_grouper.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# 运行 Flask 应用
CMD ["flask", "run"]

