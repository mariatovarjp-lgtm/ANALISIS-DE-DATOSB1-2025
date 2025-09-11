from setuptools import setup

setup(
    name="iudigital_ANALISISD",
    version="0.0.1",
    author="Maria Tovar",
    author_email="maria.tovarjp@est.iudigital.edu.co",
    description="ETL para análisis de datos del dólar",
    py_modules=["actividad1"],   
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "matplotlib"
         "kagglehub[pandas-datasets]>=0.3.8",
        "seaborn",
        "pyarrow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)