import socket, sys, time

GREEN = "\033[92m"; RED = "\033[91m"; CYAN = "\033[96m"; RESET = "\033[0m"

def print_slow(text, delay=0.05): 
 for char in text:
  sys.stdout.write(char); sys.stdout.flush()
  time.sleep(delay)
 print()

def scan_ports(target, start_port, end_port):
    print(f"\n{CYAN}" + "="*40 + f"\nscanning {target} from port {start_port} to {end_port}...\n" + "="*40 + f"{RESET}\n")
    
    results = []  
    for port in range(start_port, end_port+1): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            result = f"{GREEN}[+] port {port} is open{RESET}"
            results.append(f"port {port} is open")  
        else: result = f"{RED}[-] port {port} is closed{RESET}" 
        print(result); s.close()
    
    if results:
        with open("scan_results.txt", "w") as f:  
            f.write("\n".join(results))  
        print(f"\n{GREEN}scan complete. results saved to scan_results.txt{RESET}") 
    else: print(f"\n{RED}scan complete. no open ports found.{RESET}")

if __name__ == "__main__": 
    print_slow(f"{CYAN}port scanner initialized...{RESET}\n", delay=0.03)

    target = input("enter target ip address: ").strip()  

    try:
        start_port = int(input("enter start port: ").strip()); end_port = int(input("enter end port: ").strip())

        if start_port > end_port or start_port < 1 or end_port > 65535: 
            print(f"{RED}invalid port range. ports must be between 1 and 65535.{RESET}")
            sys.exit(1)  

        scan_ports(target, start_port, end_port)  

    except ValueError:
        print(f"{RED}please enter valid numbers for ports.{RESET}")
        sys.exit(1)  
