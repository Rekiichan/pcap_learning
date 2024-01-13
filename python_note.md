- Trong Python, những đối tượng thuộc loại sau là `mutable`:
    - list
    - dict
    - set
    - bytearray
    - Các class được định nghĩa bởi code (mặc định)

- Các đối tượng thuộc loại sau là `immutable`:
    - int
    - float
    - decimal
    - complex
    - bool
    - string
    - tuple
    - range
    - frozenset
    - bytes

- Truyền các `đối tượng` làm `tham số` của `hàm`
    - `Tham số` được truyền vào hàm luôn luôn là `đối tượng`. Với những `đối tượng` là `immutable` (`số nguyên`, `số thực`, `tuple`, v.v...) thì giá trị của nó sẽ `không thể thay đổi` được bởi hàm, nhưng nếu là `mutable` (`list`, `dict`) thì hàm lại `có thể thay đổi` giá trị `bên ngoài`.

    - Tham số của hàm là `immutable`:
        - Các đối tượng `immutable` như `số`, `tuple`, `string` được truyền vào hàm giống hệt như `list`, `set`. Nó truyền `reference` chứ không truyền `giá trị`, tức là chỉ truyền `địa chỉ bộ nhớ`. Thế nhưng vì tính chất của `immutable` là không thể thay đổi giá trị, vì vậy nếu trong nội dung của hàm mà có thay đổi giá trị của tham số, nó hoạt động khá giống với việc truyền giá trị vào. Bởi vì mỗi khi `thay đổi giá trị`, một `vùng nhớ mới` được cấp phát, nó được gán cho `tham số` nhưng không gán cho `biến` bên ngoài, vì vậy việc thay đổi giá trị này chỉ có ý nghĩa trong hàm mà thôi, còn giá trị biến ở bên ngoài không ảnh hưởng gì.

    - Tham số của hàm là `mutable`:
        - Các đối tượng `mutable` như `list`, `dict` cũng được truyền vào qua qua `reference`, tức là `địa chỉ vùng nhớ`, không khác gì các đối tượng `immutable` cả. Thế nhưng vì tính chất của `mutable`, nên vùng nhớ này hoàn toàn có thể chứa `giá trị mới` mà `không cần cấp phát` gì cả. Vì vậy, nếu một `mutable` được truyền vào hàm mà `bị thay đổi giá trị`, thì `biến bên ngoài` cũng sẽ `chứa giá trị mới`:

- `index` và `find` là 2 `function` sử dụng tìm kiếm `substring` trong string. `index` trả về `exception` nếu không tìm thấy, còn `find` thì trả về `-1`.

- `AssertionError` được `raise` bởi `assert` khi `executed`, vì vậy nó là điều kiện kích hoạt khi `False`

- `<=`, `>=` không hỗ trợ `so sánh` số với chữ

Trong Python, các `escape sequence` là một `chuỗi các ký tự` được sử dụng để biểu diễn một ký tự đặc biệt mà bạn `không thể nhập trực tiếp trong một chuỗi`. Chúng bắt đầu bằng một dấu gạch chéo ngược `(\)` theo sau là một hoặc nhiều ký tự, và cùng nhau biểu diễn một ký tự duy nhất trong chuỗi.

Dưới đây là một số `escape sequence` phổ biến trong Python:

- \n: Xuống dòng mới (newline).
- \t: Tab ngang (horizontal tab).
- \r: Trở về đầu dòng (carriage return).
- \\: Dấu gạch chéo ngược (backslash) thực sự.
- \': Dấu nháy đơn (single quote) - cho phép bạn đưa dấu nháy đơn vào trong chuỗi được bao quanh bởi dấu nháy đơn.
- \": Dấu nháy kép (double quote) - cho phép bạn đưa dấu nháy kép vào trong chuỗi được bao quanh bởi dấu nháy kép.
- \b: Backspace - xóa một ký tự.
- \f: Formfeed - dùng trong việc in trang.
- \ooo: Ký tự với giá trị octal "ooo".
- \xhh: Ký tự với giá trị hex "hh".


```python
s = 'hello'
s[0] = s[1]
```
- không thể `assign value` cho `str` vì nó là `immutable`

- exception custom của user có thể có hoặc không được kế thừa từ `exception gốc`