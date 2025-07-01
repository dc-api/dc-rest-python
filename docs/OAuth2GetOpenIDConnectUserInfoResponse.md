# OAuth2GetOpenIDConnectUserInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** |  | 
**email** | **str** |  | [optional] 
**email_verified** | **bool** |  | [optional] 
**preferred_username** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.o_auth2_get_open_id_connect_user_info_response import OAuth2GetOpenIDConnectUserInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2GetOpenIDConnectUserInfoResponse from a JSON string
o_auth2_get_open_id_connect_user_info_response_instance = OAuth2GetOpenIDConnectUserInfoResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2GetOpenIDConnectUserInfoResponse.to_json())

# convert the object into a dict
o_auth2_get_open_id_connect_user_info_response_dict = o_auth2_get_open_id_connect_user_info_response_instance.to_dict()
# create an instance of OAuth2GetOpenIDConnectUserInfoResponse from a dict
o_auth2_get_open_id_connect_user_info_response_from_dict = OAuth2GetOpenIDConnectUserInfoResponse.from_dict(o_auth2_get_open_id_connect_user_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


