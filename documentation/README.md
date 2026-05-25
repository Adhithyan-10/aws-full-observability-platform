# 📄 Project Documentation

This folder contains the complete project documentation for the **AWS Full Observability Platform** project.

The documentation provides a detailed explanation of the complete implementation including:

- Project Overview
- Architecture Design
- Technology Stack
- Monitoring Setup
- Alerting Pipeline
- CloudWatch Dashboard
- Centralized Logging Implementation
- Athena Log Analytics
- End-to-End Validation
- Results, Challenges & Future Enhancements

---

## 📘 Documentation Preview

Click below to open the complete PDF documentation:

👉 **[Click Here to View Documentation](./AWS-Observability-Platform.pdf)**

---

## Documentation Highlights

### Monitoring & Observability
- EC2 CPU monitoring
- Lambda error monitoring
- API Gateway metrics tracking
- CloudWatch metric filters
- CloudWatch alarms

### Real-Time Alerting
- SNS topic creation
- Email subscriptions
- Real-time notifications
- End-to-end alert validation

### Centralized Logging
- Lambda logs exported to S3
- CloudWatch log groups
- Log storage architecture

### Log Analytics
- Athena integration
- SQL-based log analysis
- Query execution and insights

### Dashboard Visualization
- Unified Full-Observability Dashboard
- EC2 widgets
- Lambda widgets
- API widgets
- Log widgets
- Single Value widgets

---

## Architecture Used

The implementation follows a centralized observability architecture:

Infrastructure → CloudWatch → Alarms → SNS → Email Alerts

Logs → CloudWatch Logs → S3 → Athena → Analytics

---

## Region Used

**AWS Region:** `ap-south-1 (Mumbai)`

---

Built as part of an AWS Cloud Engineering hands-on project portfolio 🚀
