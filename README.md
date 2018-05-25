# python-security-eight-ball
In this exercise you'll be creating a simple client/server socket based game to demonstrate the basics of socket server communication.

### Instructions
2. **Clone** this repository from your personal Github account:
    - Copy the HTTPS or SSH address on the page.
    - Run the command `$ git clone [SSH or HTTP address]` in your terminal to clone this repository into your DevLeague folder 
      in  your computer (you don't need to type the "$"; this is the command __prompt__, and is used to signify your terminal is ready for commands).
3. From your terminal navigate to your DevLeague folder and into the `python-security-eight-ball` assignment:
    - `$ cd DevLeague`
    - `$ ls` 
    - `cd python-security-eight-ball`
4. Open the `python-security-eight-ball` assignment in text editor and write your code in the `client.py` and `server.py` files.
5. You'll need to run your python files in two different terminals to test your code:
   - `$ cd python-security-eight-ball`
   - `$ python server.py`
   - `$ python client.py`
6. Using the examples covered in class, make your server answer questions that people would ask about the security of their computers/homes/offices, etc.....
7. You will likely need to use a `List` of `strings` and randomly select elements from the list
8. `BOSS LEVEL`: Log all of the data that gets sent to your server in a file called `audit.log`.
9. `SUPER BOSS LEVEL`: Keep a count of the number of requests that get sent to your server and `print` the count after every response.