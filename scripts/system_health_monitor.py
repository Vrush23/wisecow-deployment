import psutil
import logging

logging.basicConfig(filename='system_health.log', level=logging.INFO)

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage: {cpu_usage}%")

    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage: {memory_info.percent}%")

    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        logging.warning(f"High Disk usage: {disk_info.percent}%")

if __name__ == "__main__":
    check_system_health()
