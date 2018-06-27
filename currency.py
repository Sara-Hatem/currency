import urllib.request
import urllib.parse
import json
try:
    currencyToChange=input("Enter the currency u wanna change")
    currencyCode=[]
    currencyCode.append(currencyToChange.upper())
    currencyCode.append("_EGP")
    currencyCode="".join(currencyCode)
    variables={"q":currencyCode,"compact":'y'}
    url='http://free.currencyconverterapi.com/api/v5/convert?'
    urlSecPart=urllib.parse.urlencode(variables)
    fullUrl=url+urlSecPart
    response=urllib.request.urlopen(fullUrl)
    v = json.loads(response.read().decode('utf-8'))
    print(v)
    print(v.get(currencyCode).get('val'))
except Exception:
    print("Please Enter The Right Currency")

