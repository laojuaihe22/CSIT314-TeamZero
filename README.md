CSIT 314 - TeamZero

after clone not able to start the program using | python app.py |

mac user -> maybe just pip install all the needed package or set up the python in-build virtual environment to install all the needed package
window user -> run in cmd/powershell --> env\Scripts\activate.bat  --> and next -->  python app.py 



for window user
how to run the program (open cmd or powershell)
1. env\scripts\activate.bat (inside got all the package that you needed maybe only pymongo not able to use)
2. python app.py
3. open web browser http://127.0.0.1:5000/
4. account email: admin@gmail.com | password: 1




if you cant run because of database

run this command in your cmd : python -m pip install "pymongo[srv]"

and now
go entity/UserAccount and change to uri to "mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
