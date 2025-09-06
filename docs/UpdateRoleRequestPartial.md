# UpdateRoleRequestPartial


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
from dc_rest.models.update_role_request_partial import UpdateRoleRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoleRequestPartial from a JSON string
update_role_request_partial_instance = UpdateRoleRequestPartial.from_json(json)
# print the JSON string representation of the object
print(UpdateRoleRequestPartial.to_json())

# convert the object into a dict
update_role_request_partial_dict = update_role_request_partial_instance.to_dict()
# create an instance of UpdateRoleRequestPartial from a dict
update_role_request_partial_from_dict = UpdateRoleRequestPartial.from_dict(update_role_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


