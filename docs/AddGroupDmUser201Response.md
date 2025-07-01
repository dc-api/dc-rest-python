# AddGroupDmUser201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**last_message_id** | **str** |  | [optional] 
**flags** | **int** |  | 
**last_pin_timestamp** | **datetime** |  | [optional] 
**recipients** | [**List[UserResponse]**](UserResponse.md) |  | 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**managed** | **bool** |  | [optional] 
**application_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.add_group_dm_user201_response import AddGroupDmUser201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroupDmUser201Response from a JSON string
add_group_dm_user201_response_instance = AddGroupDmUser201Response.from_json(json)
# print the JSON string representation of the object
print(AddGroupDmUser201Response.to_json())

# convert the object into a dict
add_group_dm_user201_response_dict = add_group_dm_user201_response_instance.to_dict()
# create an instance of AddGroupDmUser201Response from a dict
add_group_dm_user201_response_from_dict = AddGroupDmUser201Response.from_dict(add_group_dm_user201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


