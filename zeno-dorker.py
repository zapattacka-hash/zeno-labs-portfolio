import sys
import urllib.parse

def generate_dorks(domain):
    print("=============================================")
    print(f"  [+] ZENO-DORKER: OSINT AUTOMATION ENGINE")
    print(f"  [+] TARGET DOMAIN: {domain}")
    print(f"  [+] OPERATOR: Zeno Labs")
    print("=============================================\n")

    # The Zeno Labs OSINT Payload Dictionary
    dorks = {
        "Exposed Gov Documents (FOUO/CUI)": f"site:{domain} ext:pdf OR ext:xlsx \"FOUO\" OR \"CUI\"",
        "Leaked Server Logs & Databases": f"site:{domain} ext:log OR ext:sql OR ext:env",
        "Hidden Admin Directories": f"site:{domain} inurl:admin OR inurl:login OR inurl:intranet",
        "Employee PII & Rosters": f"site:{domain} ext:xls OR ext:csv \"matrix\" OR \"roster\" OR \"clearance\""
    }

    for category, query in dorks.items():
        print(f"[*] THREAT VECTOR: {category}")
        print(f"    Payload: {query}")
        
        # URL encode the payload so browsers can read the special characters
        encoded_query = urllib.parse.quote_plus(query)
        print(f"    Link:    https://www.google.com/search?q={encoded_query}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[!] Usage Error. Please provide a target domain.")
        print("    Example: python3 zeno-dorker.py af.mil")
    else:
        generate_dorks(sys.argv[1])

