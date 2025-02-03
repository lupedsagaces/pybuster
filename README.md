# Pybuster

## Description
The **Pytbuster** is a Python-based tool inspired by gobuster and was designed to perform brute force attacks on web server directories. The tool is intended to be simple, making it easy to run on servers and clients with Python installed. It attempts to identify hidden directories and endpoints using a user-provided wordlist, offering an efficient solution for reconnaissance in cybersecurity.

This script simulates the behavior of the Gobuster tool but is implemented in Python, with support for multithreading to improve performance.

---

## Features
- **Directory brute force**: Tests paths on web servers using a wordlist.
- **Parallel execution**: Supports multiple threads for faster testing.
- **Customization**: Accepts various parameters to tailor execution.
- **Output to file**: Saves found results to the `pybuster_output.txt` file.
- **Interactive banner**: Displays a visual interface when starting the script.

---

## Dependencies
This script uses the following libraries:

- `requests`: For making HTTP requests.
- `argparse`: For processing command-line arguments.
- `concurrent.futures`: For managing threads.

Install the dependencies, if necessary, with:
```bash
pip install requests
```

---

## Usage
### Basic syntax:
```bash
python3 script.py -u <URL> -w <wordlist> [-t <threads>]
```

### Parameters:
| Parameter       | Description                                     | Required    | Default   |
|-----------------|-------------------------------------------------|-------------|-----------|
| `-u`, `--url`   | Base URL for brute forcing                     | Yes         | -         |
| `-w`, `--wordlist` | Path to the wordlist to be used                | Yes         | -         |
| `-t`, `--threads` | Number of threads for parallel execution       | No          | 100       |

### Examples:
1. Brute force a server with 50 threads:
```bash
python3 script.py -u http://example.com -w /usr/share/wordlists/dirb/big.txt -t 50
```

2. Brute force with the default wordlist:
```bash
python3 script.py -u http://example.com -w wordlist.txt
```

---

## How It Works
1. The script reads a wordlist containing the names of directories to be tested.
2. For each entry in the wordlist, an HTTP request is sent to `<URL>/<directory>`.
3. Responses with status codes less than 400 are considered valid and logged in the `gobuster_output.txt` file.
4. Found results are displayed in the console and saved to the file.

---

## Output
- **Console**: Displays found directories in the format:
```
[+] Found: http://example.com/admin (200)
```
- **File**: Saves the same results to the `gobuster_output.txt` file.

---

## Note
- Ensure you have permission to test the target server.
- Misusing this tool may violate local and international laws.

---

## Contributions
Contributions are welcome! If you find bugs or have suggestions, feel free to open a pull request or an issue in the repository.

---

## Contact
For questions or support, contact me at: [golaboffsec@gmail.com](mailto:golaboffsec@gmail.com).
