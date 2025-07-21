import http from "k6/http";
import { check, sleep } from "k6";

// Test configuration
export const options = {
  thresholds: {
    // Assert that 99% of requests finish within 3000ms.
    http_req_duration: ["p(99) < 3000"],
  },
  stages: [
    { duration: "10s", target: 15 },
    { duration: "30s", target: 15 },
    { duration: "10s", target: 0 },
  ],
};

// Simulated user behavior
export default function () {
  let res = http.get("http://api:5000/");
  // Validate response status
  check(res, { "status was 200": (r) => r.status == 200 });
  sleep(1);
}