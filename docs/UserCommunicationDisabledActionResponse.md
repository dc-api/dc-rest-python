# UserCommunicationDisabledActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | [**UserCommunicationDisabledActionMetadataResponse**](UserCommunicationDisabledActionMetadataResponse.md) |  | 

## Example

```python
from dc_rest.models.user_communication_disabled_action_response import UserCommunicationDisabledActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserCommunicationDisabledActionResponse from a JSON string
user_communication_disabled_action_response_instance = UserCommunicationDisabledActionResponse.from_json(json)
# print the JSON string representation of the object
print(UserCommunicationDisabledActionResponse.to_json())

# convert the object into a dict
user_communication_disabled_action_response_dict = user_communication_disabled_action_response_instance.to_dict()
# create an instance of UserCommunicationDisabledActionResponse from a dict
user_communication_disabled_action_response_from_dict = UserCommunicationDisabledActionResponse.from_dict(user_communication_disabled_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


