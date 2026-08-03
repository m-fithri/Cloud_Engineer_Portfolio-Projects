    return json.loads(secret)

# Retrieve credentials from Secrets Manager
credentials = get_secret()

# Extract the values; if AWS_REGION isn't in the secret, use the region from the session
AWS_ACCESS_KEY_ID = credentials.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = credentials.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = credentials.get("AWS_REGION", boto3.session.Session().region_name or "ap-southeast-5")