# A Python library to access IBM i / AS400 hosts with a TN5250 emulator.

This is library is built relying on first of all the `s3270` utility. It is required to have the `s3270` installed on your system - you can learn more here: [http://x3270.bgp.nu/](http://x3270.bgp.nu/)
Second, it relies on the P3270 python library. Credit goes to the original developer **Mossaab Stiri**, his code is available at [https://github.com/mstiri/p3270](https://github.com/mstiri/p3270) and it can be found at [PyPi](https://pypi.org/project/p3270/). As the P3270 library was a bit behind, I have added a lot of functionality and the updated version can for now be found here: [https://github.com/simonfaltum/p3270](https://github.com/simonfaltum/p3270). 

Most of the functionality is the same from the 3270 to the 5250 protocol. For example, moving the cursor, sending text or pressing enter. 
However, to get access to some of the more advanced functionality in the 5250 protocol, I have used IBM's own keymapping documentation [3270 keyboard mapping for Telnet servers](https://www.ibm.com/support/knowledgecenter/ssw_ibm_i_74/rzaiw/rzaiwkeybrdmap3270.htm). 



## Installation
A simple pip command brings the library to your environment: 

```pip install p3270```

__NB__: Make sure that you're using the python3 version of the pip command. 


## Usage 
Import the client class from the library:
```python 
from p5250 import P5250Client
```

Create a client object with the config options stated in the code.
```python 
my_client = P5250Client(hostName='localhost', path='c:\\wc3270\\', codePage='cp277')
```

If the s3270 program is downloaded as a .zip file or otherwise fails to be added to the path when installed, it is possible to state the path when creating the P3270Client. Otherwise, if s3270 is in the path, it is not needed.

Connect the client, and you're good to go:
```python
if not my_client.connect():
    print('Connection failed !')
    exit(1)

# Start sending your commands to the host ...
```

### Library methods:

Once the client object (P3270Client class) is created, the following methods can be used to interact with the host.
* `connect()`:
    * __Description__: Connect the client to the host
    * __Arguments__: none
* `disconnect()` 
    * __Description__: Disconenct the client from the host 
    * __Arguments__: none
* `endSession()` 
    * __Description__: End the client session 
    * __Arguments__: none
* `sendEnter()`
    * __Description__: Send the Enter key to host 
    * __Arguments__: none
* `sendF(n)`
    * __Description__: Send a F (Function) key - F1, F2, F3... F24
    * __Arguments__: <br>
        __n__ (_int_): F key number.<br>
        The number should be in the range 1..24
* `sendBackSpace()` 
    * __Description__: Send Back space to the host ()
    * __Arguments__: none
* `sendBackTab()` 
    * __Description__: Send back Tab to the host  (go to start of previous input field) 
    * __Arguments__: none
* `sendTab()` 
    * __Description__: Send Tab key to the host 
    * __Arguments__: none
* `clearScreen()` 
    * __Description__: Clear the screen 
    * __Arguments__: none
* `delChar()` 
    * __Description__: Delete character next to the cursor (ASCII DEL) 
    * __Arguments__: none
* `delField()`
    * __Description__: Delete the whole field
    * __Arguments__: none
* `eraseChar()`
    * __Description__: Erase character previous character (ASCII BS)
    * __Arguments__: none
* `moveCursorDown()` 
    * __Description__: Move cursor down 
    * __Arguments__: none
* `moveCursorUp()` 
    * __Description__: Move cursor up 
    * __Arguments__: none
* `moveCursorLeft()` 
    * __Description__: Move cursor left 
    * __Arguments__: none
* `moveCursorRight()` 
    * __Description__: Move cursor right 
    * __Arguments__: none
* `moveTo(row, col)` 
    * __Description__: Move cursor to a specific position
    * __Arguments__: <br>
        __row__ (_int_): Row position to which the cursor should be moved.<br>
        __col__ (_int_): Column position to which the cursor should be moved.
* `moveToFirstInputField()` 
    * __Description__: Move cursor to the first input field on the current screen 	
    * __Arguments__: none
* `sendText(text)` 
    * __Description__: Send text to the host 
    * __Arguments__: <br>
        __text__ (_string_): The string to send to the host
* `saveScreen(fileName, dataType)` 
    * __Description__: Save the current screen to a file 
    * __Arguments__: <br>
        __fileName__ (string): File name to which the screen will be saved.<br>
        If the file does not exist it is created, otherwise it is appended.<br>
        Files are saved under the specified name in the directory specified in the parameter `screensDir` of the configuration file. Default: `screen`<br> 
        __dataType__ (_string_): The data type of the captured screen. Supported data types are *html*, or *rtf*. Default: `html`
* `getScreen()`
    * __Description__: Get the actual screen as raw text 
    * __Arguments__: none
* `printScreen()` 
    * __Description__: Print the current screen to the standard output 
    * __Arguments__: none
* `isConnected()` 
    * __Description__: Get the connection status of the client 
    * __Arguments__: none
* `readTextAtPosition(row, col, length)` 
    * __Description__: Reads text at a row,col position and returns it 
    * __Arguments__: <br>
        __row__ (_int_): Row position on where to read.<br>
        __col__ (_int_): Column position on where to read.<br>
        __length__ (_int_): How many chars to read
* `readTextArea(row, col, rows, cols)` 
    * __Description__: Reads text area at a row,col position and returns it 
    * __Arguments__: <br>
        __row__ (_int_): Row position on where to read.<br>
        __col__ (_int_): Column position on where to read.<br>
        __rows__ (_int_): Number of rows to read down from the starting row.<br>
        __cols__ (_int_): Number of columns to read, right from the starting column.<br>
* `readTextAtPosition(row, col, expected_text)` 
    * __Description__: Will check at the given coordinates if the text appear or not. Returns true if the text was found, false if not. 
    * __Arguments__: <br>
        __row__ (_int_): Row position on where to read.<br>
        __col__ (_int_): Column position on where to read.<br>
        __expected_text__ (_string_): The text to look for
* `waitForField()` 
    * __Description__: Will wait for the field to be ready where the cursor is standing 
    * __Arguments__: none
* `trySendTextToField(text, row, col)` 
    * __Description__: Will try and write the given text at the given position. Once the text is written, it will check if the text is now shown at the screen at that position. Returns true if succeeded, false if not. 
    * __Arguments__: <br>
        __row__ (_int_): Row position on where to read.<br>
        __col__ (_int_): Column position on where to read.<br>
        __text__ (_string_): Text to write

* `rollUp()` 
    * __Description__: Will roll up a table or menu. This is usually mapped to Page Down.
    * __Arguments__: none

* `rollDown()` 
    * __Description__: Will roll down a table or menu. This is usually mapped to Page Up.
    * __Arguments__: none


All of the above methods return `True` if they succeed, and `False` otherwise. The only exceptions:
- `endSession()`, it terminates the emulation session and returns `True` in all cases.
- `readTextAtPosition`, `readTextArea`, `getScreen` all return the text they read.



### Example:

```python
from p5250 import P5250Client

# Connect and test if connection succeeded or not
if not my_client.connect():
    print('Connection failed !')
    exit(1)

# Save the home screen to a file called 'home.html'. HTML format is the default.
my_client.saveScreen(fileName='home.html')

# Send user name to the current field (user ID)
my_client.sendText('user1')

# Send TAB key to go to the next field
my_client.sendTab()

# Send the user password to the password field.
my_client.sendText('password1')

# Send Enter key to submit the current screen with field contents
my_client.sendEnter()

# Go back : F3 key
my_client.sendF(3)

# Go back again
my_client.sendF(3)

# Disconnect from the host 
my_client.disconnect()

# End the emulation session
my_client.endSession()
```


## License 
GPLv3. See the [LICENSE](LICENSE.txt) file.