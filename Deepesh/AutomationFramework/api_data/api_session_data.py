common_url = "https://api.restful-api.dev/objects"

go_rest = "https://gorest.co.in/"
get_all_users_url = f"{go_rest}/public/v2/users"
go_rest_headers = {"Authorization": "Bearer ad6b849f911b220a37b1218280ce88bfa087d8c8f82bee717fd58a47d40f1277",
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