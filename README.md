# disk-space
Python and Docker file space monitor

This project runs over a Docker installation, two containers are created, one Python based, runs the utilities to get disk information. A second container is a Rabbitmq server.

The disk space monitoring is run every minute, by a cron job defined inside the Python container, every minute, a message is sent to a Rabbitmq queue names "disk_info" containing the following information:

```json
    body_bucket = {
        "total"
        "used"
        "free"
        "percent_used"
        "timestamp"
        "message"
    }
```
