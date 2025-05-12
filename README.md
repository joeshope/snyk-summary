# Snyk Summary

This script is designed to assist with getting a summary of a Snyk Test

# How to run:

```
snyk test --json-file-output=results.json
python3 report.py
```

# Example Output

```
SNYK TEST SUMMARY
[ 115 ] TOTAL ISSUES
[ 1 CRITICAL 46 HIGH  44 MEDIUM  24 LOW ]
```
