# 2023 Playwright Video Player

This repository contains an example of integration tests based on UI testing of a real web service (player). The project was built entirely from scratch by domanina using Python, Pytest, and Playwright.

---

## Pytest + Python + Playwright

---

### Prerequisites (Before Running Locally)

1. Install the required Python packages:

   ```bash
   pip3 install -r requirements.txt
2. Install playwright and deps:

   ```bash
   playwright install
   
   playwright install-deps

---
### Running Tests

To execute the tests, use the following commands:

=== Basic Test Run ===

Run all tests with verbose output:

`pytest -v ./tests`

or simply:

`pytest -v`

=== Running with Allure Reports ===

To generate Allure reports:

`pytest -v --alluredir=allure-results`

To view the generated reports:

`allure serve allure-results`