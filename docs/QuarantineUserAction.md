# QuarantineUserAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**metadata** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.quarantine_user_action import QuarantineUserAction

# TODO update the JSON string below
json = "{}"
# create an instance of QuarantineUserAction from a JSON string
quarantine_user_action_instance = QuarantineUserAction.from_json(json)
# print the JSON string representation of the object
print(QuarantineUserAction.to_json())

# convert the object into a dict
quarantine_user_action_dict = quarantine_user_action_instance.to_dict()
# create an instance of QuarantineUserAction from a dict
quarantine_user_action_from_dict = QuarantineUserAction.from_dict(quarantine_user_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


