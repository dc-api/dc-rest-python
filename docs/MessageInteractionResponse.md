# MessageInteractionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**name** | **str** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**name_localized** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.message_interaction_response import MessageInteractionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageInteractionResponse from a JSON string
message_interaction_response_instance = MessageInteractionResponse.from_json(json)
# print the JSON string representation of the object
print(MessageInteractionResponse.to_json())

# convert the object into a dict
message_interaction_response_dict = message_interaction_response_instance.to_dict()
# create an instance of MessageInteractionResponse from a dict
message_interaction_response_from_dict = MessageInteractionResponse.from_dict(message_interaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


