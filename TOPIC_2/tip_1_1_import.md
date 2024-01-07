# TOPIC 1: Import and use modules and packages

- Sử dụng `__import__`:
```python
import pandas as pd
df = pd.DataFrame()

# 2 dòng lệnh trên sẽ tương ứng với lệnh sau
pd = __import__('pandas')
```

- Sử dụng `sys.path`, nó `lưu trữ/định nghĩa` tất cả `absolute path` của tất cả `module` đang được sử dụng trong `file` hiện tại. Ta có thể sử dụng nó để import module
```python
import sys
sys.path.append('Users/nhandt/Documents/repo/tests_python')

# func_test - file con của folder tests_python - đã được thêm
# vào list module thông qua append, định nghĩa cho system biết 
# trong file hiện tại đã được thêm vào all module của tests_python
from func_test import test
test()
```

- sử dụng `__all__` sẽ chỉ `export` những `attribute` đã được định nghĩa bên trong `__all__` khi sử dụng lệnh from ... import *, lệnh này được sử dụng để tránh việc nhiều dev sẽ lạm dụng `from .. import *` một cách bừa bãi:
```python
def test1():
    pass

def test2():
    pass

__all__ = ['test1']
```

- Sử dụng `__init__.py`: khi viết `lib`, cần thêm file `__init__.py` sử dụng để để `Python` xem một `directory/folder` là một `package`.

# TOPIC 3: the dir() function
- Nếu trong 1 `file`, chỉ sử dụng `dir()` không có `param` truyền vào, nó sẽ in ra toàn bộ `attribute` có thể sử dụng được trong nội file đó
