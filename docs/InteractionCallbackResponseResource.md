# InteractionCallbackResponseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**message** | [**MessageResponse**](MessageResponse.md) |  | 

## Example

```python
from dc_rest.models.interaction_callback_response_resource import InteractionCallbackResponseResource

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionCallbackResponseResource from a JSON string
interaction_callback_response_resource_instance = InteractionCallbackResponseResource.from_json(json)
# print the JSON string representation of the object
print(InteractionCallbackResponseResource.to_json())

# convert the object into a dict
interaction_callback_response_resource_dict = interaction_callback_response_resource_instance.to_dict()
# create an instance of InteractionCallbackResponseResource from a dict
interaction_callback_response_resource_from_dict = InteractionCallbackResponseResource.from_dict(interaction_callback_response_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


