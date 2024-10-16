import re
from collections import defaultdict

log_file = 'access.log'

error_404_count = 0
page_requests = defaultdict(int)

with open(log_file, 'r') as file:
    for line in file:
        if ' 404 ' in line:
            error_404_count += 1

        match = re.search(r'GET (.*?) HTTP/', line)
        if match:
            page = match.group(1)
            page_requests[page] += 1

print(f"Total 404 errors: {error_404_count}")
print("Most requested pages:")
for page, count in page_requests.items():
    print(f"{page}: {count} requests")
