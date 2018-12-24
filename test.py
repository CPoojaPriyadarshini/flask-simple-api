import sqlite3

db=sqlite3.connect('../templates/country.db')
db.execute("create table countryIndia (S_No int, States char(50), Capital_City char(50), Popular_Cities char(100))")
db.execute("""insert into countryIndia values (1,"Tamil Nadu","Chennai","Trichy,Madurai,Thanjavur,Kanyakumari"),(2,"Kerala","Thiruvananthapuram","Cochin,Alapuzhua,Kottayam,Thrissur"),(3,"Andhra Pradesh","Vijayawada","Tirupathi,Chithoor,Ongole,Vishakapattinam"),(4,"Telungana","Hyderabad","Warangal,Nizamabad,Secundrabad"),(5,"Karnatake","Banglore","Mangalore,Coorg,Mysore,Hampi")""")
db.commit()
