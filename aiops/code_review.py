import boto3, json, sys, pathlib

client = boto3.client("bedrock-runtime", region_name="us-east-1")

code = pathlib.Path("app/src/main/java/com/demo/App.java").read_text()

prompt = f"""
You are a senior Java + Kubernetes engineer.
Review this code and classify issues as:
CRITICAL / HIGH / MEDIUM / LOW.

Focus on:
- CPU / memory issues
- Kubernetes risks
- Threading issues

Code:
{code}
"""

response = client.invoke_model(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    body=json.dumps({
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300
    })
)

result = response["body"].read().decode()
print(result)

if "CRITICAL" in result:
    print("❌ Blocking pipeline due to CRITICAL issues")
    sys.exit(1)
