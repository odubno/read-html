# Read HTML

### Overview
This function will render raw html in a new tab of your browser. 

### Getting Started
***

```
$ git clone https://github.com/odubno/read_html.git
$ cd read_html/
$ python read_html.py
```
***

```python
from read_html import read_html
import requests

page = requests.get('http://www.nytimes.com/pages/todayspaper/')
read_html(page)
```

***