# CreateInteractionResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**data** | [**IncomingWebhookUpdateForInteractionCallbackRequestPartial**](IncomingWebhookUpdateForInteractionCallbackRequestPartial.md) |  | 

## Example

```python
from dc_rest.models.create_interaction_response_request import CreateInteractionResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInteractionResponseRequest from a JSON string
create_interaction_response_request_instance = CreateInteractionResponseRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInteractionResponseRequest.to_json())

# convert the object into a dict
create_interaction_response_request_dict = create_interaction_response_request_instance.to_dict()
# create an instance of CreateInteractionResponseRequest from a dict
create_interaction_response_request_from_dict = CreateInteractionResponseRequest.from_dict(create_interaction_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


