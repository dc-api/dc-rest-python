# CreateMessageInteractionCallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**message** | [**MessageResponse**](MessageResponse.md) |  | 

## Example

```python
from dc_rest.models.create_message_interaction_callback_response import CreateMessageInteractionCallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageInteractionCallbackResponse from a JSON string
create_message_interaction_callback_response_instance = CreateMessageInteractionCallbackResponse.from_json(json)
# print the JSON string representation of the object
print(CreateMessageInteractionCallbackResponse.to_json())

# convert the object into a dict
create_message_interaction_callback_response_dict = create_message_interaction_callback_response_instance.to_dict()
# create an instance of CreateMessageInteractionCallbackResponse from a dict
create_message_interaction_callback_response_from_dict = CreateMessageInteractionCallbackResponse.from_dict(create_message_interaction_callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


