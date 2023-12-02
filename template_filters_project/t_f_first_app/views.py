from django.shortcuts import render
import datetime 
def home(request):
    dict = {'name' : 'mahin' , 'roll' : 2 , 'age' : 18 , 'lst' : [1, 2, 3] , 'strlst' : ['1','2','3'] , 'date' : datetime.datetime.now() , "string" : "Python iS fUn" , "profiles" : [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
] , 'HTMLfile' : "<b>I</b> <button>love</button> <span>dogs</span>"}
    return render(request, 'index.html' , dict)
