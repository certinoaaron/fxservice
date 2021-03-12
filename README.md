# FX Convert

version 0.0.1

Service used to calculate exchange rate 


## General Overview

[Overview Image](https://certinotech.visualstudio.com/e4bbe547-e4b6-477f-9392-5e9d478e39b6/_apis/git/repositories/cf4dd912-28a5-4b50-9255-3925e8767944/items?path=%2Fassets%2FFXServices.png&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0 "Overview Image")

## Testing 

```bash
make test
```

## Coverage

current total covrage is 78%

```bash
----------- coverage: platform linux, python 3.8.5-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
app/__init__.py               0      0   100%
app/app.py                   33     10    70%
app/utils/__init__.py         0      0   100%
app/utils/convert.py          3      0   100%
app/utils/extract.py         20     11    45%
app/utils/response.py        25      1    96%
tests/__init__.py             0      0   100%
tests/test_fxconvert.py      22      1    95%
---------------------------------------------
TOTAL                       103     23    78%

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

