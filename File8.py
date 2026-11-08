import os

src = input()
dst = input()

with open(src, encoding="utf-8") as f:
    nums = [line.strip() for line in f if line.strip()]

with open(dst, "w", encoding="utf-8") as f:
    f.write(nums[0] + "\n")
    f.write(nums[-1] + "\n")
