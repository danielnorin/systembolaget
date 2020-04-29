import http.client, urllib.request, urllib.parse, urllib.error, base64, json, csv
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'c56449e0c61145fea19d661f96490c2e',
}
params = urllib.parse.urlencode({
})
try:
    conn = http.client.HTTPSConnection('api-extern.systembolaget.se')
    conn.request("GET", "/product/v1/product?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    products = json.loads(data)
    with open('systembolaget.csv', mode='w',) as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['ProductId', 'ProductNumber', 'ProductNameBold', 'ProductNameThin', 'Category', 'ProductNumberShort', 'ProducerName', 'SupplierName', ])
        for product in products:
            writer.writerow([product['ProductId'], product['ProductNumber'], product['ProductNameBold'], product['ProductNameThin'], product['Category'], product['ProductNumberShort'], product['ProducerName'], product['SupplierName']])
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
