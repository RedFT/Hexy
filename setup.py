from distutils.core import setup
setup(
  name = 'Hexy',         
  packages = ['hexy'],   
  version = '1.0',      
  license='MIT',        
  description = 'A library that makes working with a hexagonal lattice easier.',   
  author = 'Norbu Tsering',                   
  author_email = 'norbu.tsering.cs@gmail.com',      
  url = 'https://github.com/redft/hexy',   
  download_url = 'https://github.com/RedFT/Hexy/archive/v1.0.tar.gz',    
  keywords = ['hexy', 'coordinate', 'hexagon', 'hexagonal'],
  install_requires=[            
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 2',      
  ],
)
