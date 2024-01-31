# testing our api



import requests


# get data from api created 
response =requests.get('http://127.0.0.1:8000/user_details/') # "user_detail/{id}"
print(response.json())


#delete data from a created api

'''

id =input("enter the id you want to delete")
response=requests.delete(f"http://127.0.0.1.8000/user_details/{id}") # "user_detail/{id}"
print(response.json())

'''

# adding data inside a created api 

''' 

username1 =input("enter the user name : ")
first_name1=input("enter the user first name : ")
last_name1=input("enter the user last name : ")
email1=input("enter the Email : ")
hash1=input("paste the hash for now : ")

#creating json format to send the data tothe api
user = {
          "username":username1,
          "first_name":first_name1,
          "last_name":last_name1,
          "email":email1,
          "password":hash1
        }

headers1 ={"Content-type":"application/json"} # what kind of formatting we have used pass this along with post

#now send it
response=requests.post('http://127.0.0.1:8000/user_details/',json=user,headers=headers1)
print(response.status_code)# is its sucesses or not


'''