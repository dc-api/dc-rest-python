# UpdateMessageInteractionCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**data** | [**IncomingWebhookUpdateForInteractionCallbackRequestPartial**](IncomingWebhookUpdateForInteractionCallbackRequestPartial.md) |  | [optional] 

## Example

```python
from dc_rest.models.update_message_interaction_callback_request import UpdateMessageInteractionCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMessageInteractionCallbackRequest from a JSON string
update_message_interaction_callback_request_instance = UpdateMessageInteractionCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMessageInteractionCallbackRequest.to_json())

# convert the object into a dict
update_message_interaction_callback_request_dict = update_message_interaction_callback_request_instance.to_dict()
# create an instance of UpdateMessageInteractionCallbackRequest from a dict
update_message_interaction_callback_request_from_dict = UpdateMessageInteractionCallbackRequest.from_dict(update_message_interaction_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


