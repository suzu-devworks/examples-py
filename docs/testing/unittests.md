# Unittests

## run test

### Command unittest

```shell
python -m unittest discover
```

```shell
python -m unittest discover -s tests -p "*_test.py" -v
```

* default start directory (-s) is ```.```   
* default search pattern (-p) is ```"test*.py"```  



### Start with code.

```python

if __name__ == "__main__":
    unittest.main()
```
