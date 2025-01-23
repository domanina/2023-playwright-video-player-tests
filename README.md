# 2023 Playwright Video Player test automation script
## Pytest + Python + Playwright

## Overview


This test automation suite ensures the reliability of the player, which handles different setting for the content playback. It includes tests for both **UI** and **functional** aspects.

---
### Prerequisites (Before Running Locally)

1. Install the required Python packages:

   ```bash
   pip3 install -r requirements.txt
   ```
2. Install playwright and deps:

   ```bash
   playwright install
   
   playwright install-deps
   ```
3. Using `.env_example` file create `.env` file to load environment variables

---
## Running Tests

To execute the tests, use the following commands:

=== Basic Test Run ===

Run all tests with verbose output:
```bash
pytest -v ./tests 
```

or simply:

```bash
pytest -v
```