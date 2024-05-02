CSIT 314 - TeamZero

1. git pull origin master

2. git add .

3. git commit -m "message"

4. git push origin master

how to run the program (open cmd or powershell)
1. env\scripts\activate.bat (inside got all the package that you needed maybe only pymongo not able to use)
2. python app.py
3. open web browser http://127.0.0.1:5000/
4. account email: admin@gmail.com | password: 1




if you cant run because of database

run this command in your cmd
python -m pip install "pymongo[srv]"

and now
go entity/UserAccount and change to uri to "mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
