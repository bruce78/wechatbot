from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    content = f.read()

setup(
    name='Wechatbot',
    version='0.0.1',
    description='Wechatbot project',
    long_description=readme,
    install_requires=['itchat==1.3.10', 'requests==2.19.1'],

    author='Kevin Zhao',
    author_email='zhaomy2000@sina.com',
    url='https://github.com/zhaomy2000/flyingshui/wechatbot',
    license=content,
    packages=find_packages()
)
