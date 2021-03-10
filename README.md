# FX Covnert

version 0.0.1

Service used to calculate exchange rate 


## General Overview

[Overview Image](https://certinotech.visualstudio.com/e4bbe547-e4b6-477f-9392-5e9d478e39b6/_apis/git/repositories/cf4dd912-28a5-4b50-9255-3925e8767944/items?path=%2Fassets%2FFXServices.png&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0 "Overview Image")

## Testing

```bash
make test
```

## Usage

```bash
curl https://fxconvert/convert?from=GBP&to=USD&amount=1&date=2021-03-09
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

