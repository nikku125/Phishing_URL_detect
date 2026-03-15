import re

url =input("Enter URL: ")
score=0
if len(url)>75:  # url always under 75 lenght
    print("URL is too long")
    score+=1

if re.search(r"\b\d{1,3}(\.\d{1,3}){3}\b",url):   #checking for ip address
    print("URL uses IP Address")
    score+=1

if "@" in url:                  #check suspicious Symbol
    print("'@' symbol found")
    score+=1
                             
if "-" in url:
   print(" '-' symbol found")
   score+=1

if not url.startswith("https"):
    print("No HTTPS Not safe")
    score+=1

with open("phishing_keywords.txt") as f:
    keywords = f.read().splitlines()

for word in keywords:
    if word in url.lower():
        print(f"⚠️ Phishing keyword found: {word}")
        score += 1


if score >= 3:
    print("\n🚨 PHISHING URL DETECTED")
else:
    print("\n✅ LEGITIMATE URL")
