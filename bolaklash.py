import re

def sozlarga_bolish(matn):

    return re.findall(r'\b\w+\b', matn.lower())

def gaplarga_bolish(matn):

    return re.split(r'[.!?]+\s*', matn.strip())


matn = """

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
"""

print(gaplarga_bolish(matn))