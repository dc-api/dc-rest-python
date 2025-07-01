# AddGroupDmUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**nick** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.add_group_dm_user_request import AddGroupDmUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroupDmUserRequest from a JSON string
add_group_dm_user_request_instance = AddGroupDmUserRequest.from_json(json)
# print the JSON string representation of the object
print(AddGroupDmUserRequest.to_json())

# convert the object into a dict
add_group_dm_user_request_dict = add_group_dm_user_request_instance.to_dict()
# create an instance of AddGroupDmUserRequest from a dict
add_group_dm_user_request_from_dict = AddGroupDmUserRequest.from_dict(add_group_dm_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


