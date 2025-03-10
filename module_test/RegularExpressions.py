import re
import time

n = 1000000
# 不提前 compile
t0 = time.time()
for _ in range(n):
    re.search(r"ran", "I ran to you")
t1 = time.time()
print("不提前 compile 运行时间：", t1-t0)

# 先做 compile
ptn = re.compile(r"ran")
for _ in range(n):
    ptn.search("I ran to you")
print("提前 compile 运行时间：", time.time()-t1)

'''
text = "My phone number is 13800138000."
# Match an 11-digit phone number
pattern = r"\d{11}"
result = re.search(pattern, text)
if result:
    print("Found phone number:", result.group())
else:
    print("No matching phone number found.")

# Extract the phone number
text = "Contact us at test@example.com or demo@sample.org for more info."
# A simple regex to match email addresses
pattern = r"\w+@\w+\.\w+"
emails = re.findall(pattern, text)
print("Extracted emails:", emails)


# Replace sensitive information
text = "My bank card number is 1234567890123456."
# Replace a 16-digit number with "****"
pattern = r"\d{16}"
result = re.sub(pattern, "****", text)
print(result)

# Split a string
text = "apple,orange;banana grape"
# Split by commas, semicolons, or whitespace
pattern = r"[,\s;]+"
fruits = re.split(pattern, text)
print(fruits)

# Compile a regex pattern for a phone number format, e.g., "123-4567"
pattern = re.compile(r"\d{3}-\d{4}")

texts = [
    "My number is 123-4567.",
    "Emergency contact: 987-6543."
]

for text in texts:
    match = pattern.search(text)
    if match:
        print("Matched number:", match.group())
'''