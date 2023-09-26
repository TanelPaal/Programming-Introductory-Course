"""Email validation."""

# Write your functions here
def has_at_symbol(email: str) -> bool:
    if "@" in email:
        return True
    else:
        return False


def is_valid_username(email: str) -> bool:
    parts = email.split('@')
    if len(parts) != 2:
        return False

    username = parts[0]

    for char in username:
        if char != '.' and not char.isalnum():
            return False

    return True


def find_domain(email: str) -> str:
    parts = email.split('@')
    domain = parts[-1]
    return domain


def is_valid_domain(email: str) -> bool:
    parts = email.split('@')
    if len(parts) != 2:
        return False

    domain = parts[-1]

    if '.' not in domain:
        return False

    domain_parts = domain.split('.')
    domain_first_part = domain_parts[0]
    domain_second_part = domain_parts[-1]

    if not domain_first_part.isalpha():
        return False
    if not (3 <= len(domain_first_part) <= 10):
        return False
    if not (2 <= len(domain_second_part) <= 5 and domain_second_part.isalpha()):
        return False
    return True


def is_valid_email_address(email: str) -> bool:
    if not has_at_symbol(email):
        return False
    if not is_valid_username(email):
        return False
    if not is_valid_domain(email):
        return False
    return True


def create_email_address(domain: str, username: str):
    email = username + "@" + domain
    if is_valid_email_address(email):
        return email
    else:
        return "Cannot create a valid email address using the given parameters!"


if __name__ == '__main__':
    print("Email has the @ symbol:")
    print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
    print(has_at_symbol("joonas.kivigmail.com"))  # -> False

    print("\nUsername has no special symbols:")
    print(is_valid_username("martalumi@taltech.ee"))  # -> True
    print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
    print(is_valid_username("marta lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta@lumi@taltech.ee"))  # -> False

    print("\nFind the email domain name:")
    print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
    print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
    print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
    print(find_domain("karla@karu@yahoo.com"))  # -> yahoo.com

    print("\nCheck if the domain is correct:")
    print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
    print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
    print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
    print(is_valid_domain("pannkook@m.oos"))  # -> False

    print("\nIs the email valid:")
    print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
    print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

    print("\nCreate your own email address:")
    print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
    print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
    print(create_email_address("koobas.com", "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!

