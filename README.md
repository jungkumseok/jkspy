## jkspy - *Python* utilities

#### Dependencies

  Upon installation, jkspy will install the following Python modules: [ *pytz, Pillow* ]
  

#### Installation

##### Requirements

  The following should be installed before you install jkspy:

  1. Python 3.4 and up + Pip3 + development libraries

```
    user@localhost:~$ sudo apt-get install python3-pip python3-dev python3-setuptools 
```

  2. Pillow dependencies:
```    
    user@localhost:~$ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

* *jkspy* works strictly on Python 3 since the code assumes python *str* to be unicode *str* and *int* to behave like *long*

##### Installing *jkspy* 

  * Method 1: Getting it from PyPI
```
    user@localhost:~$ pip3 install jkspy
```    
  * Method 2: Installing from this git repository
```
    user@localhost:~$ git clone https://github.com/jungkumseok/jkspy.git
    user@localhost:~$ cd jkspy
    user@localhost:~$ python3 setup.py install
```
if you get permission error use **sudo** in front to install as root
   
#### Usage

* Method 1: As a python module

  *example.py*
```
    from jkspy.modules import crypto
    secret = crypto.sencrypt('MyN00bPa$$w0rd', "Don't show anyone")
    print(secret)
    unlocked_secret = crypto.sdecrypt('MyN00bPa$$w0rd', secret)
    print(unlocked_secret)
```
    
* Method 2: As a bash command

  jkspy installs two bash scripts: [ *jkspy, checksum* ].
  *checksum* is just a shortcut command and the same can be done by *jkspy checksum*.
  By default *jkspy* command will be able to execute functions defined in *jkspy/cmdutils.py*


  *assuming ~/example.file*
```
    # checksum example - using jkspy
    user@localhost:~$ jkspy checksum example.file
    e59ff97941044f85df5297e1c302d260
    
    user@localhost:~$ jkspy checksum example.file sha256
    d2a84f4b8b650937ec8f73cd8be2c74add5a911ba64df27458ed8229da804a26
    
    # checksum example - using checksum
    user@localhost:~$ checksum example.file
    e59ff97941044f85df5297e1c302d260
    
    user@localhost:~$ checksum example.file sha256
    d2a84f4b8b650937ec8f73cd8be2c74add5a911ba64df27458ed8229da804a26
    
    # crypto example - sencrypt
    user@localhost:~$ jkspy sencrypt MyN00bPa$$w0rd example.file
    b"e1\x9b-v\xa3<\xb5\xb4'P\xedU\x00\x0e\x1e\x9c\xcc\xad\xea\xa5\x03\x91\x14Q\x19\x83\xf4\x83\xa6\xc1&\x08\x14\x0b\x7fOgd`'\x08\x7f\xe8l\xbb:\x92"
    File [example.file.locked] successfully created.
    
    # crypto example - sdecrypt
    user@localhost:~$ jkspy sdecrypt MyN00bPa$$w0rd example.file.locked
    Hello World
    
    File [example.file.locked.unlocked] successfully created.
```
    
#### Enjoy :)