This is a repository for Staszic cryptography course.

##25.03.2015

We will try to attack AES ECB encryption mode. <br>
Should we have enough time we will discuss AES CBC padding oracle.

####Server-side files:
   1. [ECB Shuffle](25.03.2015/ecb_shuffle.py)
   2. [ECB Decode](25.03.2015/ecb_decode.py)

####Simple clients:
   1. [ECB Shuffle Client](25.03.2015/ecb_shuffle_base.py)
   2. [ECB Decode Client](25.03.2015/ecb_decode_base.py)

####Solutions:
   (Will appear after class)

Unfortunately if you want to run it on your machine you have only 2 options:
   1. Use xinetd as I did - Linux required
   2. Rewrite challenges to use networking - Python networking required
