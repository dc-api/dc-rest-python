# OAuth2GetAuthorizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**ApplicationResponse**](ApplicationResponse.md) |  | 
**expires** | **datetime** |  | 
**scopes** | **List[str]** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.o_auth2_get_authorization_response import OAuth2GetAuthorizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2GetAuthorizationResponse from a JSON string
o_auth2_get_authorization_response_instance = OAuth2GetAuthorizationResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2GetAuthorizationResponse.to_json())

# convert the object into a dict
o_auth2_get_authorization_response_dict = o_auth2_get_authorization_response_instance.to_dict()
# create an instance of OAuth2GetAuthorizationResponse from a dict
o_auth2_get_authorization_response_from_dict = OAuth2GetAuthorizationResponse.from_dict(o_auth2_get_authorization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


