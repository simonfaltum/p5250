# A Python library to access IBM i / AS400 hosts with a TN5250 emulator.

This is library is built relying on first of all the `s3270` utility. It is required to have the `s3270` installed on your system - you can learn more here: [http://x3270.bgp.nu/](http://x3270.bgp.nu/)
Second, it relies on the P3270 python library. Credit goes to the original developer **Mossaab Stiri**, his code is available at [https://github.com/mstiri/p3270](https://github.com/mstiri/p3270) and it can be found at [PyPi](https://pypi.org/project/p3270/). As the P3270 library was a bit behind, I have added a lot of functionality and the updated version can for now be found here: [https://github.com/simonfaltum/p3270](https://github.com/simonfaltum/p3270). 

Most of the functionality is the same from the 3270 to the 5250 protocol. For example, moving the cursor, sending text or pressing enter. 
However, to get access to some of the more advanced functionality in the 5250 protocol, I have used IBM's own keymapping documentation [3270 keyboard mapping for Telnet servers](https://www.ibm.com/support/knowledgecenter/ssw_ibm_i_74/rzaiw/rzaiwkeybrdmap3270.htm). 



