This is a repository for Staszic cryptography course.

##25.03.2015

We will try to attack AES ECB encryption mode. <br>
Should we have enough time we will discuss AES CBC padding oracle.

####Requirements
If you want to attack services the best way is to use [Python](https://www.python.org/) <br>
You will also need [PyCrypto](https://www.dlitz.net/software/pycrypto/) library

####Server-side files:
   1. ECB Shuffle
   	- [Original](25.03.2015/ecb_shuffle.py)
   	- [Standalone](25.03/2015/ecb_shuffle_standalone.py)
   2. ECB Decode
   	- [Original](25.03/2015/ecb_decode.py)
   	- [Standalone](25.03/2015/ecb_decode_standalone.py)

####Simple clients:
   1. [ECB Shuffle Client](25.03.2015/ecb_shuffle_base.py)
   2. [ECB Decode Client](25.03.2015/ecb_decode_base.py)

####Solutions:
   (Will appear after class)


####Running at home:
If you want to run it on your machine you have 3 options:
   1. Use xinetd as I did - Linux required
   2. Use server-side files described as standalone. You can run it anywhere.
   3. Devise something else
