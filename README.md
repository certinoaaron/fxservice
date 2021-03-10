# FX Covert

version 0.0.1

Service used to calculate exchange rate 

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

