import os

file_a = input()
file_b = input()

if os.path.exists(file_a):
    src = file_a
    dst = file_b
else:
    src = file_b
    dst = file_a

with open(src, encoding="utf-8") as f:
    nums = [line.strip() for line in f if line.strip()]

with open(dst, "w", encoding="utf-8") as f:
    f.write(nums[-1] + "\n")
    f.write(nums[0] + "\n")
