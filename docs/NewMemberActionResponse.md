# NewMemberActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | 
**action_type** | **int** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**emoji** | [**SettingsEmojiResponse**](SettingsEmojiResponse.md) |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.new_member_action_response import NewMemberActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewMemberActionResponse from a JSON string
new_member_action_response_instance = NewMemberActionResponse.from_json(json)
# print the JSON string representation of the object
print(NewMemberActionResponse.to_json())

# convert the object into a dict
new_member_action_response_dict = new_member_action_response_instance.to_dict()
# create an instance of NewMemberActionResponse from a dict
new_member_action_response_from_dict = NewMemberActionResponse.from_dict(new_member_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


