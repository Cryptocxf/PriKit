from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="prikit",
    version="1.0.0",
    author="[Cryptocxf]",
    author_email="[cryptocxf@163.com]",
    description="基于Presidio的多格式文件脱敏SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cryptocxf/PriKit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "prikit=prikit.cli:main",
        ],
    },
    include_package_data=True,
    keywords="anonymization, data-protection, privacy, presidio, pdf, word, excel, image, ppt",
    project_urls={
        "Bug Reports": "https://github.com/Cryptocxf/PriKit",
        "Source": "https://github.com/Cryptocxf/PriKit",
        "Documentation": "https://github.com/Cryptocxf/PriKit/README.md",
    },
)