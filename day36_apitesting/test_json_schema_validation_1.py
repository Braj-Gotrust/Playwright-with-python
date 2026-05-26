"""
pre-requisites:
    install dependencies:
        pip install jsonschema
"""
from jsonschema import validate, ValidationError
from playwright.sync_api import Playwright


# helper function to validate schema
def validate_json_schema(response_json, myschema):
    try:
        validate(instance=response_json, schema=myschema)
        print("Schema validation successfull")
        return True
    except ValidationError as e:
        print("schema validation failed")
        return False







def test_json_schema_validation(playwright: Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://mocktarget.apigee.net/json")

    assert response.ok

    response_body = response.json()
    print(response_body)

    # convert json to json-schema via tools
    schema = {
              "type": "object",
              "properties": {
                "firstName": {
                  "type": "string"
                },
                "lastName": {
                  "type": "string"
                },
                "city": {
                  "type": "string"
                },
                "state": {
                  "type": "string"
                }
              },
              "required": [
                "firstName",
                "lastName",
                "city",
                "state"
              ]
            }

    is_valid = validate_json_schema(response_body, schema)
    assert is_valid

    request_context.dispose()