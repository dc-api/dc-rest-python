# QuarantineUserActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | **object** |  | 

## Example

```python
from dc_rest.models.quarantine_user_action_response import QuarantineUserActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuarantineUserActionResponse from a JSON string
quarantine_user_action_response_instance = QuarantineUserActionResponse.from_json(json)
# print the JSON string representation of the object
print(QuarantineUserActionResponse.to_json())

# convert the object into a dict
quarantine_user_action_response_dict = quarantine_user_action_response_instance.to_dict()
# create an instance of QuarantineUserActionResponse from a dict
quarantine_user_action_response_from_dict = QuarantineUserActionResponse.from_dict(quarantine_user_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


