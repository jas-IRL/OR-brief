#!/usr/bin/env python3
"""
Complete PMD rebuild - careful string replacements only
"""

with open('/Users/jasbond/or-brief/orbit-pmd-disputes-new.html', 'r') as f:
    content = f.read()

# Simple string replacements - no regex, no complex patterns
replacements = [
    # Title and metadata
    ('<title>ORBIT — Brokerage Migration to FE Orem</title>', 
     '<title>ORBIT — PMD Disputes Platform Migration</title>'),
    
    ('<div class="sub">Brokerage Migration · FE Orem</div>',
     '<div class="sub">PMD Disputes · Platform Migration</div>'),
    
    ('ORBIT · BROKERAGE MIGRATION · FE OREM',
     'ORBIT · PMD DISPUTES PLATFORM MIGRATION'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('/Users/jasbond/or-brief/orbit-pmd-disputes-new.html', 'w') as f:
    f.write(content)

print(f"File has {len(content.splitlines())} lines")
print("Basic replacements complete. File structure preserved.")
