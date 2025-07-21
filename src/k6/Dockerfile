FROM grafana/k6:latest
WORKDIR /app

COPY k6-load-tests.js /k6-load-tests.js
RUN chmod +x /k6-load-tests.js