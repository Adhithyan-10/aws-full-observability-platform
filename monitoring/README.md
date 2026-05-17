## Amazon SNS Topic Configuration

![SNS Topic](1-SNS-Topic-Created.png)

An Amazon SNS topic named **EC2-Alerts** was created to handle notification delivery for CloudWatch alarms. This topic acts as the communication layer between CloudWatch and subscribed users.

---

## Email Subscription Setup

![SNS Subscription](2-SNS-Subscription-(Email).png)

An email subscription endpoint was attached to the SNS topic. This enables CloudWatch alarms to deliver notifications directly through email.

---

## Subscription Confirmation

![Subscription Confirmation](3-Email-Confirmation.png)

The email subscription request was successfully confirmed.

---

## EC2 Monitoring Configuration

![EC2 Instance](4-EC2-Instance-Running.png)

An EC2 instance was selected and used as the infrastructure resource for monitoring CPU metrics.

---

## CPU Alarm Configuration

![CPU Alarm Configuration](5-CPU-Alarm-Configuration.png)

A CloudWatch alarm was configured for EC2 CPU utilization monitoring.

---

## CPU Alarm Created

![CPU Alarm Created](6-CPU-Alarm-Created.png)

The EC2 CPU alarm was successfully created and linked with SNS notifications.
