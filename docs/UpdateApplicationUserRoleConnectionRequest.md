# UpdateApplicationUserRoleConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_name** | **str** |  | [optional] 
**platform_username** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dc_rest.models.update_application_user_role_connection_request import UpdateApplicationUserRoleConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicationUserRoleConnectionRequest from a JSON string
update_application_user_role_connection_request_instance = UpdateApplicationUserRoleConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicationUserRoleConnectionRequest.to_json())

# convert the object into a dict
update_application_user_role_connection_request_dict = update_application_user_role_connection_request_instance.to_dict()
# create an instance of UpdateApplicationUserRoleConnectionRequest from a dict
update_application_user_role_connection_request_from_dict = UpdateApplicationUserRoleConnectionRequest.from_dict(update_application_user_role_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


