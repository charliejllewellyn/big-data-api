import json
import prestodb

def lambda_handler(event, context):
    print(event)
    country = event['name']
    conn=prestodb.dbapi.connect(
    host='ip-10-0-0-6.eu-west-2.compute.internal',
    port=8889,
    user='the-user',
    catalog='hive',
    )
    cur = conn.cursor()
    query = 'SELECT * FROM tpsds.customer where "c_birth_country"=\'' + country + "'"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(rows)
    }

