import requests
from bs4 import BeautifulSoup

#emails = []

temp_emails =""

def get_website_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    emails = soup.find_all("a", href=lambda href: href and "mailto:" in href)
    email_list = [email.get_text() for email in emails]

    return emails
"""
def convert_name_to_email(name):
    print("name: ", name)
    name_parts = name.split()

    if len(name_parts) == 2:
        first_name = name_parts[0].lower()
        last_name = name_parts[1].lower()

        email = f"{first_name}.{last_name}@os-ajdovscina.si"
        return email

    elif len(name_parts) == 3:
        first_name = name_parts[0].lower()
        middle_name = name_parts[2].lower()
        last_name = name_parts[1].lower()
        email = f"{first_name}.{last_name}-{middle_name}@os-ajdovscina.si"
        return email
    else:
        return None
    
email = convert_name_to_email(emails)
if email:
        print(f"Email: {email}")
else:
        print("Neuspešno")    

"""

url = "https://osdl.splet.arnes.si/zaposleni/elektronski-naslovi-vseh-delavcev-sole-v-solskem-letu-201819/"
emails = get_website_info(url)
print("Emails:", emails)
