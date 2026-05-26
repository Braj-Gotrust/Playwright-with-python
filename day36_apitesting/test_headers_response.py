from playwright.sync_api import Playwright


def test_headers_response(playwright: Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://www.google.com/")

    assert response.ok
    # or
    assert response.status_text == "OK"

    assert response.status == 200

    # contains all header data
    headers = response.headers
    for key, value in headers.items():
        print(f"{key}: {value}")

    #  validate specific header key and value
    content_type = headers.get("content-type") # It is acept only lower character text
    print(f"{content_type}")
    assert "text/html" in content_type # in opetator fetch partial text
    assert headers.get("content-encoding") == "gzip"

    # validate specific header key presence
    assert "server" in headers
    assert "set-cookie" in headers

