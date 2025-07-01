# InteractionCallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction** | [**InteractionResponse**](InteractionResponse.md) |  | 
**resource** | [**InteractionCallbackResponseResource**](InteractionCallbackResponseResource.md) |  | [optional] 

## Example

```python
from dc_rest.models.interaction_callback_response import InteractionCallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionCallbackResponse from a JSON string
interaction_callback_response_instance = InteractionCallbackResponse.from_json(json)
# print the JSON string representation of the object
print(InteractionCallbackResponse.to_json())

# convert the object into a dict
interaction_callback_response_dict = interaction_callback_response_instance.to_dict()
# create an instance of InteractionCallbackResponse from a dict
interaction_callback_response_from_dict = InteractionCallbackResponse.from_dict(interaction_callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


