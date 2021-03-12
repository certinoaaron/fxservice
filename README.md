# FX Convert

Internal service used to calculate exchange rates using fxdata as it's cache/data layer



## General Overview

[Overview Image](https://certinotech.visualstudio.com/e4bbe547-e4b6-477f-9392-5e9d478e39b6/_apis/git/repositories/cf4dd912-28a5-4b50-9255-3925e8767944/items?path=%2Fassets%2FFXServices.png&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0 "Overview Image")

## Testing 

```bash
make test
```

## Coverage

current total coverage is 73%

```bash
$ make coverage
pytest --cov=app tests/
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /home/aaron/Desktop/Projects/fxservice
plugins: cov-2.11.1
collected 2 items                                                                                                                                                                                                 

tests/test_fxconvert.py ..                                                                                                                                                                                  [100%]

----------- coverage: platform linux, python 3.8.5-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
app/__init__.py             0      0   100%
app/app.py                 33     10    70%
app/utils/__init__.py       0      0   100%
app/utils/convert.py        3      0   100%
app/utils/extract.py       20     11    45%
app/utils/response.py      25      1    96%
-------------------------------------------
TOTAL                      81     22    73%

```

## Auto format
re-format's code to PEP 8 standard

```bash
make format
```

## Build

```bash
make build
```

## Deploy Locally
Deploy using docker-compose

```bash
docker-compose up
```

## Usage

```bash
curl http://fxconvert/convert?from=GBP&to=USD&amount=1&date=2021-03-09
```

if successful the command should return 

```json
{
    "success": true,
    "query": {
        "from": "GBP",
        "to": "USD",
        "amount": 1 
    },
  
    "date": "2021-03-09",
    "rate": 1.2,
    "result": 1.20
}
```

