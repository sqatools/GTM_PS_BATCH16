common_url = "https://api.restful-api.dev/objects"

go_rest = "https://www.gorest.co.in/"
get_all_users_url = f"{go_rest}/public/v2/users"
go_rest_header = {"Authorization" : "Bearer 7e17415d0bf1e0f36b3df5ade76ca5ebeb60f1fc6281eb97ef7ee85b403ea663",
                   "Content-Type" : "application/json"}


post_request_data = {
            "name": "Apple MacBook Pro 200",
            "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
        }
headers = {"Content-Type" : "application/json"}