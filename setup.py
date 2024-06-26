# coding: utf-8
# ref: https://packaging.python.org/tutorials/packaging-projects/
import os
import setuptools
import re

DESCRIPTION = 'PyGuitar generates an easy-to-practice chord book.'

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open(os.path.join(here, "guitar/__init__.py"), "r") as file:
    pattern = re.compile(r'^(\w+)\s*=\s*"([^"]+)"')
    for line in file.read().splitlines():
        match = re.match(pattern, line)
        if match is not None and match[1] == "__version__":
            version = match[2]
            break
    else:
        raise RuntimeError("couldn't get version!")

print(version)

def setup_package():
    metadata = dict(
        name='PyGuitar',
        version=version,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        author='Shuto Iwasaki',
        author_email='cabernet.rock@gmail.com',
        license='MIT',
        project_urls={
            'Source Code': 'https://github.com/iwasakishuto/PyGuitar',
        },
        packages=setuptools.find_packages(),
        package_data={'guitar': ['data/*']},
        python_requires=">=3.6",
        install_requires=[
            # 'numpy>=1.15.1',
            'matplotlib>=2.2.4',
            # 'seaborn>=0.10.0',
        ],
        extras_require={
          'tests': ['pytest'],
        },
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Other Audience',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        entry_points = {
            "console_scripts": [
                "ufret=guitar.main:export_ufret_chordbooks",
            ],
        },
    )
    setuptools.setup(**metadata)

if __name__ == "__main__":
    setup_package()
