# Utils_Add_Batch_Unique_ID

**AddBatchTag.py** to create new batch tag

**CopyBatchTag.py** to create box using the latest batch tag

Please make sure to change the center path to your own path:



```python
......
import uuid

# Change this path to create a Tag Center
TAG_CENTER_PATH = r'XXXX\TagCenter'


def add_info(file_name='README', info = ''):

    if not '.md' in file_name:
        file_name = file_name+'.md'
	......
```

