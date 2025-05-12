import json

def analyze_vulnerabilities(json_data):
    """
    Parses the provided JSON data to summarize vulnerability information.

    Args:
        json_data (dict): A dictionary representing the JSON vulnerability data.

    Returns:
        None: Prints the vulnerability summary to the console.
    """

    vulnerabilities = json_data.get("vulnerabilities", [])
    total_issues = len(vulnerabilities)
    severity_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}

    # ANSI color codes
    colors = {
        "SNYK": "\033[95m",         # Purple
        "CRITICAL": "\033[91m",     # Red
        "HIGH": "\033[38;5;208m",   # Orange
        "MEDIUM": "\033[93m",       # Yellow
        "LOW": "\033[90m",          # Dark Gray/Grey
        "RESET": "\033[0m"          # Reset to default color
    }

    for vuln in vulnerabilities:
        severity = vuln.get("severity", "UNKNOWN").upper()
        if severity in severity_counts:
            severity_counts[severity] += 1

    print(f"{colors.get('SNYK', '')}SNYK TEST SUMMARY{colors['RESET']}")
    print(f"[ {total_issues} ] TOTAL ISSUES")
    print(
        f"[ "
        f"{colors.get('CRITICAL', '')}{severity_counts.get('CRITICAL', 0)} CRITICAL {colors['RESET']}"
        f"{colors.get('HIGH', '')}{severity_counts.get('HIGH', 0)} HIGH  {colors['RESET']}"
        f"{colors.get('MEDIUM', '')}{severity_counts.get('MEDIUM', 0)} MEDIUM  {colors['RESET']}"
        f"{colors.get('LOW', '')}{severity_counts.get('LOW', 0)} LOW {colors['RESET']}]"
    )

if __name__ == "__main__":
    json_data = json.loads(open('results.json').read())
    analyze_vulnerabilities(json_data)