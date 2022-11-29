from setuptools import find_packages, setup

setup(
    name="project_layout_setup",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=['streamlit',]
)