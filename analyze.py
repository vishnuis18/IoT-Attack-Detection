Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd

df = pd.read_csv("C:/Users/vishn/OneDrive/Documents/FDS/your_file.csv")
print(df.head())
SyntaxError: multiple statements found while compiling a single statement
import pandas as pd


df = pd.read_csv("C:/Users/vishn/OneDrive/Documents/FDS/your_file.csv")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    df = pd.read_csv("C:/Users/vishn/OneDrive/Documents/FDS/your_file.csv")
  File "C:\Users\vishn\AppData\Roaming\Python\Python312\site-packages\pandas\io\parsers\readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\vishn\AppData\Roaming\Python\Python312\site-packages\pandas\io\parsers\readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\vishn\AppData\Roaming\Python\Python312\site-packages\pandas\io\parsers\readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\vishn\AppData\Roaming\Python\Python312\site-packages\pandas\io\parsers\readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "C:\Users\vishn\AppData\Roaming\Python\Python312\site-packages\pandas\io\common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/vishn/OneDrive/Documents/FDS/your_file.csv'
import pandas as pd

df = pd.read_csv("C:/Users/vishn/OneDrive/Documents/FDS/UNSW_2018_IoT_Botnet_Final_10_Best.csv")
print(df.head())
SyntaxError: multiple statements found while compiling a single statement
import pandas as pd
df = pd.read_csv("C:/Users/vishn/OneDrive/Documents/FDS/UNSW_2018_IoT_Botnet_Final_10_Best.csv")
print(df.head())
SyntaxError: multiple statements found while compiling a single statement
import pandas as pd
df = pd.read_csv("C:/Users/vishn/OneDrive/Documents/FDS/UNSW_2018_IoT_Botnet_Final_10_Best.csv")
print(df.head())
  ;pkSeqID;proto;saddr;sport;daddr;dport;seq;stddev;N_IN_Conn_P_SrcIP;min;state_number;mean;N_IN_Conn_P_DstIP;drate;srate;max;attack;category;subcategory
0  0;1;tcp;192.168.100.147;49960;192.168.100.7;80...                                                                                                     
1  1;2;arp;192.168.100.7;-1;192.168.100.147;-1;10...                                                                                                     
2  2;3;tcp;192.168.100.147;49962;192.168.100.7;80...                                                                                                     
3  3;4;tcp;192.168.100.147;49964;192.168.100.7;80...                                                                                                     
4  4;5;tcp;192.168.100.147;49966;192.168.100.7;80...                                                                                                     
import pandas as pd
df = pd.read_csv("C:/Users/vishn/OneDrive/Documents/FDS/UNSW_2018_IoT_Botnet_Final_10_Best.csv", sep=';')


Warning (from warnings module):
  File "<pyshell#10>", line 1
DtypeWarning: Columns (4,6) have mixed types. Specify dtype option on import or set low_memory=False.
print(df.head())
   Unnamed: 0  pkSeqID proto  ... attack category subcategory
0           0        1   tcp  ...      1      DoS        HTTP
1           1        2   arp  ...      1      DoS        HTTP
2           2        3   tcp  ...      1      DoS        HTTP
3           3        4   tcp  ...      1      DoS        HTTP
4           4        5   tcp  ...      1      DoS        HTTP

[5 rows x 20 columns]
print(df.describe())
         Unnamed: 0       pkSeqID  ...           max        attack
count  3.668522e+06  3.668522e+06  ...  3.668522e+06  3.668522e+06
mean   1.834260e+06  1.834262e+06  ...  3.020015e+00  9.998700e-01
std    1.059011e+06  1.059011e+06  ...  1.860877e+00  1.140212e-02
min    0.000000e+00  1.000000e+00  ...  0.000000e+00  0.000000e+00
25%    9.171302e+05  9.171312e+05  ...  2.806072e-01  1.000000e+00
50%    1.834260e+06  1.834262e+06  ...  4.009111e+00  1.000000e+00
75%    2.751391e+06  2.751392e+06  ...  4.293582e+00  1.000000e+00
max    3.668521e+06  3.668522e+06  ...  4.999999e+00  1.000000e+00

[8 rows x 13 columns]
print(df['attack'].value_counts())
attack
1    3668045
0        477
Name: count, dtype: int64
print(df['category'].value_counts())
category
DDoS              1926624
DoS               1650260
Reconnaissance      91082
Normal                477
Theft                  79
Name: count, dtype: int64
>>> print(df['proto'].value_counts())
proto
udp          1996437
tcp          1662812
icmp            9052
arp              213
ipv6-icmp          8
Name: count, dtype: int64
>>> import seaborn as sns
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
>>> import seaborn as sns
... import matplotlib.pyplot as plt
... 
... sns.countplot(x='attack', data=df)
... plt.title("Attack vs Normal")
... plt.show()
SyntaxError: multiple statements found while compiling a single statement
>>> import seaborn as sns
... import matplotlib.pyplot as plt
SyntaxError: multiple statements found while compiling a single statement
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> sns.countplot(x='attack', data=df)
<Axes: xlabel='attack', ylabel='count'>
>>> plt.show()
>>> sns.countplot(x='category', data=df)
<Axes: xlabel='category', ylabel='count'>
>>> plt.xticks(rotation=45)
([0, 1, 2, 3, 4], [Text(0, 0, 'DoS'), Text(1, 0, 'DDoS'), Text(2, 0, 'Normal'), Text(3, 0, 'Reconnaissance'), Text(4, 0, 'Theft')])
>>> plt.title("Types of Attacks")
Text(0.5, 1.0, 'Types of Attacks')
>>> plt.show()
>>> sns.countplot(x='proto', data=df)
<Axes: xlabel='proto', ylabel='count'>
>>> plt.title("Protocol Distribution")
Text(0.5, 1.0, 'Protocol Distribution')
>>> plt.show()
