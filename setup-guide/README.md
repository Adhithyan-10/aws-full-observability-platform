# Setup Guide

## Overview

This guide explains the complete implementation workflow used to build the **AWS Full Observability Platform**. The project combines infrastructure monitoring, centralized logging, alerting, dashboards, and log analytics using AWS services.

---

# Architecture Flow

Monitoring Layer

EC2 / Lambda / API Gateway  
↓  
CloudWatch Metrics + Logs  
↓  
Metric Filters  
↓  
CloudWatch Alarms  
↓  
Amazon SNS  
↓  
Email Notifications  
↓  
Dashboard Visualization

---

Logging Layer

Lambda Application  
↓  
CloudWatch Logs  
↓  
Amazon S3  
↓  
Athena Query Engine  
↓  
Log Analytics

---

# Phase 1: SNS Alert Configuration

### Step 1

Create an SNS Topic

Example:

```text
EC2-Alerts
```

Purpose:

Used as the centralized notification system for alarms.

---

### Step 2

Create an email subscription endpoint.

Purpose:

Allows CloudWatch alarms to send email notifications.

---

### Step 3

Confirm the email subscription.

Purpose:

Enables SNS notification delivery.

---

# Phase 2: Infrastructure Monitoring

### Step 1

Launch an EC2 instance.

Purpose:

Provides infrastructure metrics for monitoring.

---

### Step 2

Select metric:

```text
CPUUtilization
```

Threshold:

```text
Greater than 70%
```

---

### Step 3

Create CloudWatch alarm.

Attach:

SNS Topic

Purpose:

Trigger notifications during high CPU usage.

---

# Phase 3: Lambda Monitoring

### Step 1

Select Lambda functions.

Examples:

- TokenExchange
- GeneratepreSignedURL
- secureAPI

---

### Step 2

Choose metric:

```text
Errors
```

Threshold:

```text
Greater than 0
```

Purpose:

Detect Lambda failures.

---

# Phase 4: API Monitoring

### Step 1

Open API Gateway metrics.

Monitor:

- 4XX Errors
- 5XX Errors

Purpose:

Track API failures.

---

### Step 2

Create CloudWatch alarm.

Attach SNS notifications.

---

# Phase 5: Log Monitoring

### Step 1

Open CloudWatch Log Groups.

Select Lambda log group.

Example:

```text
/aws/lambda/TokenExchange
```

---

### Step 2

Create metric filter:

Pattern:

```text
ERROR
```

Metric:

```text
ErrorCount
```

---

### Step 3

Create second metric filter:

Pattern:

```text
Exception
```

Metric:

```text
ExceptionCount
```

Purpose:

Convert logs into measurable CloudWatch metrics.

---

### Step 4

Create alarms using generated metrics.

Purpose:

Automatically detect application failures.

---

# Phase 6: Dashboard Creation

Create CloudWatch dashboard:

```text
Full-Observability-Dashboard
```

Add widgets:

- EC2 CPU Widget
- Lambda Widget
- API Widget
- Log Widget
- Number Widget

Purpose:

Provide centralized monitoring.

---

# Phase 7: Centralized Logging Pipeline

### Step 1

Create Lambda logging function.

Purpose:

Generate application logs.

---

### Step 2

Execute Lambda function.

Purpose:

Generate INFO, DEBUG and SUCCESS logs.

---

### Step 3

Export CloudWatch logs to Amazon S3.

Purpose:

Enable centralized log storage.

---

### Step 4

Configure S3 Bucket Policy.

Purpose:

Allow CloudWatch export permissions.

---

### Step 5

Configure Athena query result location.

Example:

```text
s3://central-logs-adhithyan/athena-results/
```

---

### Step 6

Create Athena external table.

Purpose:

Enable SQL querying over logs.

---

### Step 7

Run Athena queries.

Example:

```sql
SELECT * FROM lambda_logs LIMIT 10;
```

---

# Final Outcome

Successfully implemented:

✅ Infrastructure Monitoring  
✅ Lambda Monitoring  
✅ API Monitoring  
✅ Log-Based Monitoring  
✅ Real-Time Alerts  
✅ Dashboard Visualization  
✅ Centralized Logging  
✅ Athena Log Analytics  
✅ End-to-End Observability

---

# Key Learning

Observability combines:

- Metrics
- Logs
- Alerts
- Dashboards
- Analytics

Together these provide complete visibility into system health.
