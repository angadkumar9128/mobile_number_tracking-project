import opencellid

api = opencellid.Client(api_key='YOUR_API_KEY')
response = api.cell.get(mcc=310, mnc=410, lac=1234, cellid=5678)
print(response)