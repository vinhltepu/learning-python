 Biểu thức chính quy (regular expression hay regex) là một công cụ mạnh mẽ được sử dụng để tìm kiếm, khớp và thao tác
chuỗi văn bản (strings). Biểu thức chính quy giúp định nghĩa mẫu (pattern) của chuỗi văn bản mà bạn muốn tìm hoặc thao
tác
+ Tìm kiếm văn bản 
+ Thay thế văn bản 
+ Kiểm tra tính hợp lệ (validation)
+ Phân tích văn bản (parsing)
+ Lọc dữ liệu 

ctrl + f để mở tìm kiếm trên visual 

Cú pháp    Ý nghĩa
.          Bất kỳ ký tự nào, ngoại trừ ký tự xuống dòng (new line)
\d         Chữ số (0-9)
\D         Không phải chữ số (0-9)
\w         Ký tự từ vựng (a-z, A-Z, 0-9, _)
\W         Không phải ký tự từ vựng
\s         Ký tự trắng (dấu cách, tab, xuống dòng)
\S         Không phải ký tự trắng
\b         Ranh giới từ (Word Boundary)
\B         Không phải ranh giới từ
^          Bắt đầu của một chuỗi
$          Kết thúc của một chuỗi
[]         Khớp với các ký tự trong dấu ngoặc vuông
[^ ]       Khớp với các ký tự KHÔNG có trong dấu ngoặc vuông
|          Hoặc
()         Nhóm (group)


Các toán tử định lượng (Quantifiers):
Cú pháp    Ý nghĩa
*          0 hoặc nhiều lần
+          1 hoặc nhiều lần
?          0 hoặc 1 lần
{3}        Chính xác số lần (ví dụ: 3 lần)
{3,4}      Số lần trong phạm vi (ví dụ: từ 3 đến 4 lần)



version en:

.          - Any Character Except New Line
\d         - Digit (0-9)
\D         - Not a Digit (0-9)
\w         - Word Character (a-z, A-Z, 0-9, _)
\W         - Not a Word Character
\s         - Whitespace (space, tab, newline)
\S         - Not Whitespace (space, tab, newline)

\b         - Word Boundary
\B         - Not a Word Boundary
^          - Beginning of a String
$          - End of a String

[]         - Matches Characters in brackets
[^ ]       - Matches Characters NOT in brackets
|          - Either Or
( )        - Group


- Tham chiếu ngược trong regex (regular expressions) là một cách sử dụng lại nội dung của một nhóm đã được khớp trong mẫu tìm kiếm.
Nó cho phép bạn tham chiếu lại một phần của chuỗi mà bạn đã bắt (capture) trong các nhóm ngoặc đơn ().

- Cách sử dụng tham chiếu ngược (backreference):
+ Sử dụng trong phần tìm kiếm (search): Bạn có thể tham chiếu đến các nhóm đã bắt được trong regex với cú pháp \n, trong đó n là số thứ tự của nhóm.
+ Sử dụng trong phần thay thế (replacement): Khi thay thế chuỗi, bạn cũng có thể sử dụng tham chiếu ngược để thay thế bằng nội dung của nhóm. Sử dụng $n trong đó n là số thứ tự của nhóm