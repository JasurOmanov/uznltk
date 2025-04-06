from setuptools import setup, find_packages

setup(
    name="uznltk",
    version="0.1.0",
    packages=find_packages(),
    author="Khamidullayevich Software",
    description="O‘zbek tili uchun tabiiy tilni qayta ishlash vositasi",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",  # <-- faqat shuni yozing, matn emas
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
