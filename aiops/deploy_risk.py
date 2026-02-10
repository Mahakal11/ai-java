import sys, pathlib, boto3, json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

yaml = pathlib.Path("helm/templates/deployment.yaml").read_text()

prompt = f"""
Review this Kubernetes deployment.
Flag CRITICAL issues like:
- No resource limits
- Single replica
- No probes

Deployment:
{yaml}
"""

resp = client.invoke_model(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    body=json.dumps({
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    })
)

result = resp["body"].read().decode()
print(result)

if "CRITICAL" in result:
    sys.exit(1)
