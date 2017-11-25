# Read HTML

### Overview
This function will render raw html in a new tab of your browser. 


```python
from read_html import read_html
import requests

page = requests.get('http://www.nytimes.com/pages/todayspaper/')
read_html(page)
```