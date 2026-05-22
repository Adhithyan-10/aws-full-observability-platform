# Architecture Overview

This folder contains the high-level architecture diagram of the **AWS Full Observability Platform**, illustrating the complete flow of centralized monitoring, centralized logging, alerting, dashboards, and log analytics implemented in this project.

The architecture combines AWS services to provide **real-time visibility**, **error tracking**, **centralized log analysis**, and **automated alerting** across infrastructure and application components.

---

## Architecture Diagram

![AWS Full Observability Architecture](./AWS-Full-Observability-Architecture.png)


---

## Architecture Components

### Application Layer

The application layer represents the components generating requests and application events.

Components:

- **Users** → Access application APIs
- **Amazon API Gateway** → Handles incoming API requests
- **AWS Lambda Functions**
  - TokenExchange
  - GeneratePreSignedURL
  - secureAPI
  - authFunction
- **Amazon EC2**
  - Infrastructure component monitored for CPU metrics

Lambda functions generate logs and metrics that flow into the observability pipeline.

---

## Monitoring & Observability Layer

AWS CloudWatch is used as the centralized monitoring platform.

### CloudWatch Metrics

Monitored metrics include:

- EC2 CPU Utilization
- Lambda Errors
- Lambda Duration
- API Gateway 4XX Errors
- API Gateway 5XX Errors

---

### Log-Based Metrics

CloudWatch Metric Filters convert logs into custom metrics:

- ERROR
- ExceptionCount
- ErrorCount

These metrics enable advanced monitoring and alert generation.

---

### CloudWatch Alarms

CloudWatch alarms continuously monitor thresholds:

- EC2 CPU alarms
- Lambda alarms
- API alarms
- Log metric alarms

When thresholds are crossed, alarms trigger SNS notifications.

---

### CloudWatch Dashboard

A centralized dashboard provides a unified view of:

- EC2 CPU Widget
- Lambda Error Widget
- API Error Widget
- Log Error Widget
- Single Value Widget

Dashboard name:

```text
Full-Observability-Dashboard
```

---

## Alerting Layer

Amazon SNS handles real-time alert delivery.

Flow:

```text
CloudWatch Alarm
        ↓
SNS Topic
        ↓
Subscription
        ↓
Email Notification
```

Alerts generated:

- High CPU utilization
- Lambda errors
- API failures
- Application exceptions
- Log-based errors

---

## Centralized Logging Pipeline

The project implements centralized log collection and analysis.

Flow:

```text
CloudWatch Logs
        ↓
Export to S3
        ↓
Centralized S3 Bucket
        ↓
Athena Query Engine
        ↓
Athena Results Bucket
```

S3 bucket stores logs for long-term analysis.

---

## Log Analytics

Amazon Athena is used to query centralized logs.

Sample queries:

### View Logs

```sql
SELECT * 
FROM lambda_logs
LIMIT 10;
```

### Count Error Logs

```sql
SELECT COUNT(*)
FROM lambda_logs
WHERE log_level='ERROR';
```

### Count Exceptions

```sql
SELECT COUNT(*)
FROM lambda_logs
WHERE log_message LIKE '%Exception%';
```

---

## End-to-End Observability Flow

```text
Infrastructure / Applications
              ↓
CloudWatch collects Metrics & Logs
              ↓
CloudWatch Alarms trigger
              ↓
SNS sends notifications
              ↓
Logs centralized in S3
              ↓
Athena performs analysis
              ↓
CloudWatch Dashboard provides visibility
```

---

## AWS Services Used

- Amazon EC2
- AWS Lambda
- Amazon API Gateway
- Amazon CloudWatch
- Amazon SNS
- Amazon S3
- Amazon Athena
- IAM Roles & Policies
- CloudWatch Logs

---

## Key Benefits

✅ Centralized monitoring across infrastructure and applications

✅ Real-time alerting for critical failures

✅ Centralized logging architecture

✅ Query-based log analytics

✅ Unified dashboard visibility

✅ Scalable and cost-effective observability solution

---

This architecture demonstrates an end-to-end AWS observability implementation integrating monitoring, alerting, logging, and analytics into a centralized platform.
