from setuptools import setup

setup(name='neon-py',
      version='0.1.0',
      description='Neon common library',
      author='Rozhkov Dmitrii',
      author_email='dr@neonlabs.org',
      license='GPL-3.0',
      url='https://neonlabs.org/',
      packages=["neon_py", "neon_py.network", "neon_py.utils"],
      install_requires=[],
      long_description="",
      long_description_content_type="text/markdown",
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
      ],
)
