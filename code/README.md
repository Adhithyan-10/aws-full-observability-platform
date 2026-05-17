# Source Code

This folder contains the AWS Lambda source code used in the logging component of the AWS Full Observability Platform.

## Purpose

The Lambda function simulates application activity and generates logs that flow through the centralized logging pipeline.

Generated log types:

- INFO logs
- DEBUG logs
- SUCCESS logs
- ERROR logs (when exceptions occur)

## Logging Flow

Lambda
↓
CloudWatch Logs
↓
S3 Central Storage
↓
Athena Analytics

## Files

### lambda_logging.py

Python Lambda function used for:

- Generating application logs
- Testing centralized logging
- Producing CloudWatch log events
- Simulating real-world monitoring scenarios

This function acts as the application's logging source within the observability platform.

