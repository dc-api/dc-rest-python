# UpdateMessageInteractionCallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**message** | [**MessageResponse**](MessageResponse.md) |  | 

## Example

```python
from dc_rest.models.update_message_interaction_callback_response import UpdateMessageInteractionCallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMessageInteractionCallbackResponse from a JSON string
update_message_interaction_callback_response_instance = UpdateMessageInteractionCallbackResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateMessageInteractionCallbackResponse.to_json())

# convert the object into a dict
update_message_interaction_callback_response_dict = update_message_interaction_callback_response_instance.to_dict()
# create an instance of UpdateMessageInteractionCallbackResponse from a dict
update_message_interaction_callback_response_from_dict = UpdateMessageInteractionCallbackResponse.from_dict(update_message_interaction_callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


