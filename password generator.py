#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[19]:


import string
import secrets


def generate_password(length: int, special_characters: bool):
    num_digits = length // 4
    num_special_characters = length // 5
    num_letters = length - (num_digits + num_special_characters)
    num_uppercase, num_lowercase = num_letters // 3, num_letters // 3
    num_letters -= num_uppercase + num_lowercase
    pool = (
        "".join(secrets.choice(string.ascii_uppercase) for _ in range(num_uppercase))
        + "".join(secrets.choice(string.ascii_lowercase) for _ in range(num_lowercase))
        + "".join(secrets.choice(string.ascii_letters) for _ in range(num_letters))
        + "".join(secrets.choice(string.digits) for _ in range(num_digits))
    )

    if special_characters:
        pool += "".join(
            secrets.choice(string.punctuation) for _ in range(num_special_characters)
        )
    p_list = list(pool)
    secrets.SystemRandom().shuffle(p_list)

    return "".join(p_list)


def main():
    print("Password Generator")
    p_len = input("Enter the length of the password [12-32] (default: 16): ").strip()

    if p_len:
        try:
            p_len = int(p_len)

            if p_len not in range(8, 33):
                raise ValueError

        except ValueError:
            return print("Invalid length entered!")
    p_sp_chr = input("Do you need special characters (!@#$%)? [Yes/No]: ")
    if p_sp_chr.lower() not in ["yes", "no"]:
        return print("Invalid response!")
    res = generate_password(
        length=p_len if p_len else 16,
        special_characters=True if p_sp_chr.lower() == "yes" else False,
    )
    print(f"Generated Password: {res}")
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




