import base64
from email.mime import base

from playwright.sync_api import Playwright


# # Basic authentication - 1
# # url - https://httpbin.org/basic-auth/user/pass
# # username -user
# # password - pass
# def test_basic_authentication(playwright: Playwright):
#     request_context = playwright.request.new_context()
#     credentials = base64.b64encode(b'user:pass').decode('utf-8')
#     response = request_context.get("https://httpbin.org/basic-auth/user/pass", headers = {"Authorization": f"Basic {credentials}"})
#
#     assert response.status == 200
#     response_body = response.json()
#     print("Response body: ", response_body)
#
#     request_context.dispose()




# # Basic authentication - 2
# # url - https://the-internet.herokuapp.com/basic_auth
# # username -admin
# # password - admin
# def test_basic_authentication(playwright: Playwright):
#     request_context = playwright.request.new_context()
#     credentials = base64.b64encode(b'admin:admin').decode('utf-8')
#     response = request_context.get("https://the-internet.herokuapp.com/basic_auth", headers = {"Authorization": f"Basic {credentials}"})
#
#     assert response.status == 200
#     # response_body = response.json()   # this page is not json formate
#     response_body = response.text()   # this is return the data with text formate not a json formate
#
#     print("Response body: ", response_body)
#
#     request_context.dispose()





# Bearer Token authentication
# url - https://api.github.com/users/Braj-Gotrust/repos
# url - https://api.github.com/user/repos
def test_bearer_token_auth_github_repos(playwright: Playwright):
    token = "abc"

    request_context = playwright.request.new_context()
    response = request_context.get("https://api.github.com/users/Braj-Gotrust/repos", headers = {"Authorization": f"Bearer {token}"})

    assert response.status == 200
    response_body = response.json()   # this page is not json formate

    print("Response body (Repositories...): ", response_body)

    request_context.dispose()
