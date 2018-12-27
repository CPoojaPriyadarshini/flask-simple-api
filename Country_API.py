from flask import Flask, request
from flask_restful import Resource,Api
from sqlalchemy import create_engine

db=create_engine('sqlite:///country.db')
app=Flask(__name__)
api=Api(app)

class info(Resource):
    def get(self):
        conn = db
        query = conn.execute("select * from countryIndia") 
        #return {'info': [i[0:] for i in query.fetchall()]} 
        return{'data': [dict(zip(tuple(query.keys()) ,i)) for i in query]}

class S_No(Resource):
    def get(self,S_No):
        conn=db
        query=conn.execute("select * from countryIndia where S_No="+str(S_No))
        return {'data': [dict(zip(tuple(query.keys()) ,i)) for i in query]}

class States(Resource):
    def get(self,States):
        conn=db
        query=conn.execute("select * from countryIndia where States like '%s'" % States)
        return {'data': [dict(zip(tuple(query.keys()) ,i)) for i in query]}

api.add_resource(info,'/')
api.add_resource(S_No,'/S_No/<S_No>')
api.add_resource(States,'/States/<States>')

app.run()
