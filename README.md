# Install Operation

### This project should have python3 environment, no more than python 3.5 
```
python3 setup.py install
```

### Use pyinstaller to create platform dependent application

``` 
pip3 install pyinstaller
``` 

### or pointer to the destination source

```
pip3 install pyinstaller -i https://pypi.doubanio.com/simple
```

### start to create platform dependent application file

```
pyinstaller --onefile wechatbot.py
```