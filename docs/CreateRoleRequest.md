# CreateRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**permissions** | **int** |  | [optional] 
**color** | **int** |  | [optional] 
**hoist** | **bool** |  | [optional] 
**mentionable** | **bool** |  | [optional] 
**icon** | **str** |  | [optional] 
**unicode_emoji** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.create_role_request import CreateRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleRequest from a JSON string
create_role_request_instance = CreateRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRoleRequest.to_json())

# convert the object into a dict
create_role_request_dict = create_role_request_instance.to_dict()
# create an instance of CreateRoleRequest from a dict
create_role_request_from_dict = CreateRoleRequest.from_dict(create_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


