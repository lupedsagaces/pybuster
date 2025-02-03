import requests
from concurrent.futures import ThreadPoolExecutor
import argparse

def print_banner():
    banner = """
 ██▓███▓██   ██▓▄▄▄▄   █    ██  ██████▄▄▄█████▓█████ ██▀███  
▓██░  ██▒██  ██▓█████▄ ██  ▓██▒██    ▒▓  ██▒ ▓▓█   ▀▓██ ▒ ██▒
▓██░ ██▓▒▒██ ██▒██▒ ▄█▓██  ▒██░ ▓██▄  ▒ ▓██░ ▒▒███  ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░ ▐██▓▒██░█▀ ▓▓█  ░██░ ▒   ██░ ▓██▓ ░▒▓█  ▄▒██▀▀█▄  
▒██▒ ░  ░░ ██▒▓░▓█  ▀█▒▒█████▓▒██████▒▒ ▒██▒ ░░▒████░██▓ ▒██▒
▒▓▒░ ░  ░ ██▒▒▒░▒▓███▀░▒▓▒ ▒ ▒▒ ▒▓▒ ▒ ░ ▒ ░░  ░░ ▒░ ░ ▒▓ ░▒▓░
░▒ ░    ▓██ ░▒░▒░▒   ░░░▒░ ░ ░░ ░▒  ░ ░   ░    ░ ░  ░ ░▒ ░ ▒░
                                    By: lupedsagaces
    """
    print(banner)

def check_directory(url, directory):
    full_url = f"{url}/{directory}"
    try:
        response = requests.get(full_url, timeout=5, allow_redirects=True)
        if response.status_code < 400:  # Considera apenas respostas válidas
            print(f"[+] Found: {full_url} ({response.status_code})")
            with open("gobuster_output.txt", "a") as output_file:
                output_file.write(f"[+] {full_url} ({response.status_code})\n")
    except requests.RequestException:
        pass  # Ignora erros

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Python Gobuster script")
    parser.add_argument("-u", "--url", required=True, help="Base URL to brute force")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads (default: 100)")
    args = parser.parse_args()

    url = args.url
    wordlist_path = args.wordlist
    threads = args.threads

    # Carrega a wordlist
    try:
        with open(wordlist_path, "r") as wordlist:
            directories = [line.strip() for line in wordlist if line.strip()]
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        return

    print("Starting directory brute force...")

    # Usa ThreadPoolExecutor para rodar em paralelo
    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(lambda directory: check_directory(url, directory), directories)

if __name__ == "__main__":
    main()
