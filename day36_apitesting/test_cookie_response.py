from playwright.sync_api import Playwright


def test_cookies_response(playwright: Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://www.google.com/")

    assert response.ok
    # or
    assert response.status_text == "OK"
    assert response.status == 200

    # extract all the cookies form the response
    cookies = request_context.storage_state()["cookies"]

    for c in cookies:
        print(f"{c['name']}=>{c['value']}=>{c['domain']}")


    # check if "AEC" cookie is exist
    aec_cookie = None
    for c in cookies:
        if c["name"] == "AEC":
            aec_cookie = c
            break
    assert aec_cookie is not None, "AEC cookie not found"

    # printing details of AEC cookies
    print("AEC cookies details :")
    print(aec_cookie['name'])
    print(aec_cookie['value'])
    print(aec_cookie['domain'])
    print(aec_cookie['path'])
    print(aec_cookie['expires'])

