from distutils.core import setup
setup(
  name = 'Hexy',         
  packages = ['hexy'],   
  version = '1.4',      
  license='MIT',        
  description = 'A library that makes working with a hexagonal lattice easier.',   
  author = 'Norbu Tsering',                   
  author_email = 'norbu.tsering.cs@gmail.com',      
  url = 'https://github.com/redft/hexy',   
  download_url = 'https://github.com/RedFT/Hexy/archive/1.4.tar.gz',    
  keywords = ['hexy', 'coordinate', 'hexagon', 'hexagonal'],
  install_requires = ["numpy == 1.15.0"],
  extras_require ={            
      'examples': [
        "atomicwrites (==1.1.5)",
        "attrs (==18.1.0)",
        "funcsigs (==1.0.2)",
        "more-itertools (==4.3.0)",
        "pathlib2 (==2.3.2)",
        "pluggy (==0.7.1)",
        "py (==1.5.4)",
        "pygame (==1.9.4)",
        "pytest (==3.7.0)",
        "scandir (==1.7)",
        "six (==1.11.0)",
        ]
      },
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 2',      
  ],
)
