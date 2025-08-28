from setuptools import setup, find_packages

setup(
    name="iudigital_ANALISISD",
    version="0.0.1",
    author="Maria Tovar",
    author_email="maria.tovarjp@est.iudigital.edu.co",
    description="ETL para análisis de datos del dólar",
    py_modules=["actividad1", "actividad2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "matplotlib"
    ]
)