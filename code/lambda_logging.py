import json
import time

def lambda_handler(event, context):
    print("INFO: Lambda started")
    print("DEBUG: Processing request")

    # Simulate processing time
    time.sleep(1)

    try:
        result = 10 / 2
        print(f"SUCCESS: Computation done {result}")
    except Exception as e:
        print(f"ERROR: {str(e)}")

    print("INFO: Lambda completed")

    return {
        'statusCode': 200,
        'body': json.dumps('Logging test successful')
    }
