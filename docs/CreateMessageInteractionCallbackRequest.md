# CreateMessageInteractionCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**data** | [**IncomingWebhookInteractionRequest**](IncomingWebhookInteractionRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.create_message_interaction_callback_request import CreateMessageInteractionCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageInteractionCallbackRequest from a JSON string
create_message_interaction_callback_request_instance = CreateMessageInteractionCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMessageInteractionCallbackRequest.to_json())

# convert the object into a dict
create_message_interaction_callback_request_dict = create_message_interaction_callback_request_instance.to_dict()
# create an instance of CreateMessageInteractionCallbackRequest from a dict
create_message_interaction_callback_request_from_dict = CreateMessageInteractionCallbackRequest.from_dict(create_message_interaction_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


