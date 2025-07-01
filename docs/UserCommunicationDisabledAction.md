# UserCommunicationDisabledAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | [**UserCommunicationDisabledActionMetadata**](UserCommunicationDisabledActionMetadata.md) |  | 

## Example

```python
from dc_rest.models.user_communication_disabled_action import UserCommunicationDisabledAction

# TODO update the JSON string below
json = "{}"
# create an instance of UserCommunicationDisabledAction from a JSON string
user_communication_disabled_action_instance = UserCommunicationDisabledAction.from_json(json)
# print the JSON string representation of the object
print(UserCommunicationDisabledAction.to_json())

# convert the object into a dict
user_communication_disabled_action_dict = user_communication_disabled_action_instance.to_dict()
# create an instance of UserCommunicationDisabledAction from a dict
user_communication_disabled_action_from_dict = UserCommunicationDisabledAction.from_dict(user_communication_disabled_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


