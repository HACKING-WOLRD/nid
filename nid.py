
import os, sys, time, random, shutil

# ========== COLORS ==========
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
B = '\033[1;34m'; C = '\033[1;36m'; M = '\033[1;35m'
W = '\033[1;37m'; K = '\033[90m'; RESET = '\033[0m'

def clear(): os.system('clear' if os.name != 'nt' else 'cls')

def typewrite(text, delay=0.006):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner(title, secs=2.2):
    frames = ['|','/','-','\\']
    sys.stdout.write(Y + title + " "); t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        sys.stdout.write(frames[i % 4]); sys.stdout.flush()
        time.sleep(0.10); sys.stdout.write('\b'); i += 1
    print(G + "✓" + RESET)

def progress_bar(title, width=36, duration=1.8):
    sys.stdout.write(C + title + "\n")
    steps = max(1, int(duration / 0.04))
    for i in range(steps + 1):
        filled = int(i / steps * width)
        bar = "█" * filled + "░" * (width - filled)
        pct = int(i / steps * 100)
        sys.stdout.write(M + f"[{bar}] {pct:3d}%\r" + RESET)
        sys.stdout.flush(); time.sleep(0.04)
    print()

def neon_banner():
    clear()
    art = [
        f"{M}███╗   ██╗███╗   ██╗██████╗  ██████╗ ██╗███╗   ██╗ ██████╗",
        f"{C}████╗  ██║████╗  ██║██╔══██╗██╔═══██╗██║████╗  ██║██╔════╝",
        f"{B}██╔██╗ ██║██╔██╗ ██║██████╔╝██║   ██║██║██╔██╗ ██║██║  ███╗",
        f"{G}██║╚██╗██║██║╚██╗██║██╔══██╗██║   ██║██║██║╚██╗██║██║   ██║",
        f"{Y}██║ ╚████║██║ ╚████║██║  ██║╚██████╔╝██║██║ ╚████║╚██████╔╝",
        f"{R}╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝{RESET}"
    ]
    for ln in art: print(ln); time.sleep(0.02)
    print(W + "                       H A C K I N G   W O R L D™" + RESET)
    print(K + "           VIP Number Information — ROOT ONLY (WORK)" + RESET)
    print(W + "────────────────────────────────────────────────────────\n")

def require_root():
    has_geteuid = hasattr(os, "geteuid")
    euid_ok = (os.geteuid() == 0) if has_geteuid else False
    su_path = shutil.which("su") or shutil.which("tsu")
    if not euid_ok and not su_path:
        print(R + "\n[✘] Root Access Not Found!" + RESET)
        print(Y + "[!] This tool requires ROOT. Use 'tsu'/'su' to open a root shell and run again." + RESET)
        input(W + "\nPress Enter to exit…" + RESET); sys.exit(1)
    if has_geteuid and os.geteuid() != 0:
        print(R + "\n[✘] Not running as root (effective UID != 0)." + RESET)
        print(C + "Tip: In Termux run: " + W + "tsu" + C + " then: " + W + "python number_info_root.py" + RESET)
        input(W + "\nPress Enter to exit…" + RESET); sys.exit(1)
    print(G + "[✓] Root privileges verified." + RESET); time.sleep(0.6)

def confetti(lines=2, width=60):
    syms = ['✦','✧','✪','✺','✹','✱','✲']
    cols = [R,G,Y,B,C,M,W]
    for _ in range(lines):
        print("".join(random.choice(cols)+random.choice(syms)+RESET for _ in range(width)))
        time.sleep(0.02)

# --------- Fake Data Pools ----------
NAMES = ["Rakib Hasan","Tamanna Akter","Sajib Rahman","Nusrat Jahan",
         "Atik Khan","Mehedi Hasan","Mahiya Akter","Sumaiya Islam",
         "Arif Hossain","Shanto Saha","Niloy Ahmed","Sadia Khatun"]
FATHERS = ["Abdul Karim","Jalal Uddin","Kamrul Hasan","Shafiqul Islam","Abdul Mannan","Nazrul Islam"]
MOTHERS = ["Rokeya Begum","Salma Akter","Shirin Sultana","Hasina Khatun","Fouzia Parvin","Laila Khatun"]
AREAS  = ["Dhaka, Bangladesh","Chattogram, Bangladesh","Barishal, Bangladesh",
          "Sylhet, Bangladesh","Khulna, Bangladesh","Rajshahi, Bangladesh","Rangpur, Bangladesh"]
CARRIERS = ["GP","Robi","Banglalink","Teletalk"]

def fake_lookup(number):
    # Visual pipeline
    spinner("[*] Mounting privileged session", 1.6)
    progress_bar("[#] Syncing fingerprint & tokens", 40, 1.6)
    spinner("[*] Attaching kernel namespace", 1.4)
    progress_bar("[#] Query pipeline (visual only)", 36, 1.6)

    # Generate fake profile
    nid = str(random.randint(1000000000, 9999999999))
    name = random.choice(NAMES)
    father = random.choice(FATHERS)
    mother = random.choice(MOTHERS)
    area = random.choice(AREAS)
    carrier = random.choice(CARRIERS)
    sim_date = f"{random.randint(2014,2024)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
    age = random.randint(18, 55)
    blood = random.choice(["A+","A-","B+","B-","O+","O-","AB+","AB-"])

    print()
    confetti(3, 56)
    print(G + ">>> RESULT ( DATA ONLY)" + RESET)
    print(W + "──────────────────────────────────────────────" + RESET)
    print(G + f"[✓] Phone Number      : {W}{number}")
    print(G + f"[✓] Carrier           : {W}{carrier}")
    print(G + f"[✓] NID Number        : {W}{nid}")
    print(G + f"[✓] Full Name         : {W}{name}")
    print(G + f"[✓] Father’s Name     : {W}{father}")
    print(G + f"[✓] Mother’s Name     : {W}{mother}")
    print(G + f"[✓] Present Address   : {W}{area}")
    print(G + f"[✓] Age               : {W}{age}")
    print(G + f"[✓] Blood Group       : {W}{blood}")
    print(G + f"[✓] SIM Registered On : {W}{sim_date}")
    print(W + "──────────────────────────────────────────────" + RESET)
    print(K + "NOTE: All information above is RANDOM &  (for /work only)." + RESET)

def main():
    neon_banner()
    require_root()  # enforce root-only

    number = input(C + "[+] Enter Phone Number: " + W).strip()
    if not number:
        print(R + "Phone number is required. Exiting." + RESET); return

    # quick cosmetic validation
    if not number.replace('+','').replace('-','').isdigit():
        print(Y + "[!] Non-standard format detected, continuing (visual only)..." + RESET)
        time.sleep(0.8)

    fake_lookup(number)
    input(W + "\nPress Enter to exit…" + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "\nInterrupted by user.\n")