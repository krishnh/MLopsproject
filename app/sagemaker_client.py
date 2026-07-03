import json
import os
from typing import Tuple

import boto3


AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
SAGEMAKER_ENDPOINT_NAME = os.getenv(
    "SAGEMAKER_ENDPOINT_NAME",
    "mlops-sample-endpoint"
)

runtime = boto3.client("sagemaker-runtime", region_name=AWS_REGION)


def invoke_sagemaker(age: int, salary: float) -> Tuple[str, float]:
    payload = {
        "age": age,
        "salary": salary
    }

    response = runtime.invoke_endpoint(
        EndpointName=SAGEMAKER_ENDPOINT_NAME,
        ContentType="application/json",
        Body=json.dumps(payload)
    )

    result = json.loads(response["Body"].read().decode("utf-8"))

    return result["risk"], float(result["score"])