# 2023_playwright_player
Example of automation test repo with tests based on a real service(player). Created by domanina from scratch
---
Pytest+python+playwright
---
Before running (locally)
---
`pip3 install -r requirements.txt`

`playwright install`

`playwright install-deps`

---
Run UI and Functional tests
---
run tests:
`pytest -v`

Allure
---

run with Allure reports:

`pytest -v --alluredir=allure-results`

start Allure:

`allure serve allure-results`