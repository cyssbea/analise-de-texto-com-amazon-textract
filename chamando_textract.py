import boto3

client = boto3.client(
    'textract',
    region_name='us-east-2'
)

with open(lista_escola.png, rb) as f
    img = f.read()

response = client.detect_document_text(
    Document={'Bytes' img}
)

for block in response['Blocks']
    if block['BlockType'] == 'LINE'
        print(block['Text'])
