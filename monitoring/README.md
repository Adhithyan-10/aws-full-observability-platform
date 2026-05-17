# Monitoring Implementation Details

## Amazon SNS Topic Configuration

![SNS Topic](1-SNS-Topic-Created.png)

An Amazon SNS topic named **EC2-Alerts** was created to handle notification delivery for CloudWatch alarms. This topic acts as the communication layer between CloudWatch and subscribed users.

---

## Email Subscription Setup

![SNS Subscription](2-SNS-Subscription-(Email).png)

An email endpoint was subscribed to the SNS topic. This enables CloudWatch alarms to deliver notifications directly through email.

---

## Subscription Confirmation

![Subscription Confirmation](3-Email-Confirmation.png)

The email subscription request was successfully confirmed. Once confirmed, AWS begins delivering notifications generated from alarms.

---

## EC2 Monitoring Configuration

![EC2 Instance](4-EC2-Instance-Running.png)

An EC2 instance was selected and used as the infrastructure resource for monitoring CPU metrics and alarm testing.

---

## CPU Alarm Configuration

![CPU Alarm Configuration](5-CPU-Alarm-Configuration.png)

A CloudWatch alarm was configured for EC2 CPU utilization monitoring using threshold-based evaluation.

---

## CPU Alarm Created

![CPU Alarm Created](6-CPU-Alarm-Created.png)

The EC2 CPU alarm was successfully created and connected with SNS notifications.

---

## Lambda Function Selection

![Lambda Functions](7-Lambda-Function-List.png)

Available Lambda functions were selected for centralized monitoring and error tracking.

---

## Lambda Error Alarm Setup

![Lambda Error Alarm Setup](8-Lambda-Error-Alarm-Setup.png)

CloudWatch error metrics for Lambda functions were selected and configured.

---

## Lambda Alarm Created

![Lambda Alarm Created](9-Lambda-Alarm-Created.png)

A Lambda alarm was created to detect function failures and execution issues.

---

## API Gateway Metrics Selection

![API Metrics](10-API-Gateway-Metrics-Selection.png)

API Gateway metrics were selected to monitor request failures and API health.

---

## API Alarm Created

![API Alarm](11-API-Alarm-Created.png)

API monitoring alarms were created for tracking API failures.

---

## CloudWatch Log Group

![Log Group](12-Log-Group-View.png)

CloudWatch Log Groups were configured to store application-generated logs.

---

## ERROR Metric Filter

![Metric Filter ERROR](13-Metric-Filter-ERROR.png)

A metric filter was configured to identify ERROR patterns from logs and convert them into CloudWatch metrics.

---

## EXCEPTION Metric Filter

![Metric Filter EXCEPTION](14-Metric-Filter-EXCEPTION.png)

A second metric filter was created to detect Exception patterns generated from application logs.

---

## Custom Metrics Visible

![Custom Metrics](15-Custom-Metrics-Visible.png)

Custom metrics generated from metric filters became available in CloudWatch.

---

## Log Alarms Created

![Log Alarms](16-Log-Alarms-Created.png)

CloudWatch alarms were created using log-derived metrics for automatic failure detection.

---

## Dashboard Created

![Dashboard Created](17-Dashboard-Created.png)

A centralized dashboard named **Full-Observability-Dashboard** was created.

---

## EC2 CPU Widget

![EC2 CPU Widget](18-EC2-CPU-Widget.png)

Dashboard widgets were configured to display EC2 CPU utilization trends.

---

## Lambda Monitoring Widget

![Lambda Monitoring Widget](19-Lambda-Monitoring-Widget.png)

Lambda monitoring widgets provide visibility into function execution and failures.

---

## API Monitoring Widget

![API Monitoring Widget](20-API-Monitoring-Widget.png)

API Gateway widgets display request metrics and API health information.

---

## Log Monitoring Widget

![Log Monitoring Widget](21-Log-Monitoring-Widget.png)

A dedicated widget tracks ErrorCount and ExceptionCount metrics generated through CloudWatch log filters.

---

## Number Widget

![Number Widget](22-Number-Widget.png)

Number widgets provide instant visibility into live application error metrics.

---

## Final Dashboard View

![FINAL DASHBOARD VIEW](23-FINAL-DASHBOARD-VIEW.png)

The centralized dashboard combines infrastructure metrics, APIs, Lambda metrics, logs and monitoring widgets into one observability view.

---

## Email Alert Received

![Email Alert](24-email-Alert-recieved.png)

CloudWatch successfully triggered SNS notifications and delivered email alerts after thresholds were exceeded.

Monitoring flow:

CloudWatch Metrics  
↓  
CloudWatch Alarm  
↓  
Amazon SNS  
↓  
Email Notification

---

## Outcome

Successfully implemented a production-style AWS monitoring and observability setup capable of:

- Infrastructure monitoring
- Lambda monitoring
- API monitoring
- Log-based monitoring
- Custom metric creation
- Dashboard visualization
- Real-time alert delivery
