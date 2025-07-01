# ApplicationUserRoleConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_name** | **str** |  | [optional] 
**platform_username** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dc_rest.models.application_user_role_connection_response import ApplicationUserRoleConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUserRoleConnectionResponse from a JSON string
application_user_role_connection_response_instance = ApplicationUserRoleConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationUserRoleConnectionResponse.to_json())

# convert the object into a dict
application_user_role_connection_response_dict = application_user_role_connection_response_instance.to_dict()
# create an instance of ApplicationUserRoleConnectionResponse from a dict
application_user_role_connection_response_from_dict = ApplicationUserRoleConnectionResponse.from_dict(application_user_role_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


