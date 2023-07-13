from setuptools import setup, find_packages

setup(
    name="python-gpt-course",
    version="1.0.0",
    author="菠菜",
    author_email="daijun4you@163.com",
    description="用于ChatGPT技术课程相关的示例",
    long_description=open("README.md").read(),
    url="https://github.com/daijun4you/python-gpt-course",
    packages=find_packages(),
    requires=">=3.6"
)
