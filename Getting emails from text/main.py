import re
import functools

text_file_name = "text.txt"
exclude_text_file_name = "exclude.txt"
output_text_file_name = "output2.txt"

# email_pattern = r"\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+"
# email_pattern = r"\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}"
email_pattern = r"[a-zA-Z_.]+@[a-zA-Z.]+"
email_pattern = r"\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}"

text = ""
list_of_input_emails = list()
list_of_excluded_emails = list()
list_of_final_emails = list()


def string_length_differences(a:str, b:str)-> bool:
    return len(a) == len(b), "{}|{}".format(a,b)

def extract_emails(text:str)->list[str]:
    assert isinstance(text, str)
    ans = [m.group(0) for m in re.finditer(email_pattern, text)]
    assert isinstance(ans, list), ans
    assert all((isinstance(ele, str) for ele in ans)), type(ans[0])
    # assert all(functools.reduce(string_length_differences, ans))
    return ans

def clean_email_list(emails:list[str])->list[str]:
    assert isinstance(emails, list)
    assert all((isinstance(ele, str) for ele in emails))
    # Ensure no whitespace
    pre_ans = [ele.strip() for ele in emails]
    # Remove duplicates
    # ans = list(set(pre_ans))
    lowers = [ele.lower() for ele in pre_ans]
    lowers_unique = list(set(lowers))
    ans = pre_ans.copy()
    for an in ans:
        if an.lower() in lowers_unique:
            ans.remove(an)
    """ 
    lowers = [ele.lower() for ele in pre_ans]
    ans = pre_ans.copy()
    for lower, norm in zip(lowers, pre_ans):
        if lowers.count(lower) > 1:
            ans.remove(norm) """
    # Output
    assert isinstance(ans, list)
    assert all((isinstance(ele, str) for ele in ans))
    return ans


# MAIN
print("Regular Expression pattern: {}".format(email_pattern))
# Extract emails from text file
with open(text_file_name) as file:
    text = "\n".join(file.readlines())
    list_of_input_emails = extract_emails(text)
n_input_emails = len(list_of_input_emails)
# Clean-up emails
list_of_input_emails = clean_email_list(list_of_input_emails)
# Monitoring input
n_input_emails_cleaned = len(list_of_input_emails)
n_text = len(text)
print("Number of input emails: {}".format(n_input_emails))
print("Number of input emails cleaned: {}".format(n_input_emails_cleaned))
print("Size of text: {}".format(n_text))
# Don't waste time.
assert n_input_emails > 0, "No emails were found."

# Extract exception emails from text file
with open(exclude_text_file_name) as file:
    text = "\n".join(file.readlines())
    list_of_excluded_emails = extract_emails(text)
n_excluded_emails = len(list_of_excluded_emails)
# Clean-up emails
list_of_excluded_emails = clean_email_list(list_of_excluded_emails)
# Monitoring
print("Number of excluded emails: {}".format(n_excluded_emails))

# Create new text file with final list of emails
list_of_input_emails_lower = [ele.lower() for ele in list_of_input_emails]
list_of_final_emails = list_of_input_emails.copy()
for excluded in list_of_excluded_emails:
    exclude_key_email = excluded.lower().strip()
    if exclude_key_email in list_of_input_emails_lower:
        list_of_final_emails.remove(excluded)
# Sort output
list_of_final_emails.sort()
# Monitoring
n_final_emails = len(list_of_final_emails)
assert n_final_emails > 0, list_of_final_emails
assert n_final_emails <= n_input_emails, "{}<={}".format(n_final_emails, n_input_emails)
# Write to output file
with open(output_text_file_name, mode="wt") as file:
    for email in list_of_final_emails:
        file.write(email)
        file.write("\n")
# Monitoring
n_final_emails = len(list_of_final_emails)
print("Number of final emails: {}".format(n_final_emails))
