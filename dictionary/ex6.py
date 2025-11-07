'''Loop Through Dictionary

Given:
marks = {"math": 90, "science": 85, "english": 88}

print:
Subject: math → Marks: 90
Subject: science → Marks: 85
Subject: english → Marks: 88
'''

marks = {"math": 90, "science": 85, "english": 88}
for k, v in marks.items():
    print(f"Subject: {k} → Marks: {v}")
