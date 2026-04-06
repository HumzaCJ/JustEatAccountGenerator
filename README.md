# Just Eat Account Generator
This is an extremely simple and lightweight Python tool for automating Just Eat account creation, built as an exploration into raw HTTP-based web automation beyond traditional browser tools and automation.

## Background
This project emerged from my desire to expand beyond browser-based automation frameworks like Selenium and Playwright. Through direct HTTP requests and TLS fingerprinting, it provided hands-on experience with:
- **TLS Client Spoofing** — Mimicking browser fingerprints to bypass basic bot detection
- **API Reverse Engineering** — Understanding how web applications communicate under the hood
- **Request Header Analysis** — Crafting authentic-looking requests that mirror real browser behaviour

## How It Works
The script interfaces directly with Just Eat's consumer registration API, generating randomised user credentials via Faker and submitting them through a TLS-spoofed session that emulates Chrome.

## Requirements
```
tls_client
faker
```
<sup>you can remove faker if you want to use your own infromation instead and just don't want to go through the actual sign up process</sup>

## Disclaimer
This project is open-sourced purely for **educational purposes** to understand web automation techniques. Automated account creation violates Just Eat's Terms of Service. Use responsibly and at your own risk.

