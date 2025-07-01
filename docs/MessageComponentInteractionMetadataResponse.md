# MessageComponentInteractionMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**authorizing_integration_owners** | **Dict[str, str]** |  | 
**original_response_message_id** | **str** |  | [optional] 
**interacted_message_id** | **str** |  | 

## Example

```python
from dc_rest.models.message_component_interaction_metadata_response import MessageComponentInteractionMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageComponentInteractionMetadataResponse from a JSON string
message_component_interaction_metadata_response_instance = MessageComponentInteractionMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(MessageComponentInteractionMetadataResponse.to_json())

# convert the object into a dict
message_component_interaction_metadata_response_dict = message_component_interaction_metadata_response_instance.to_dict()
# create an instance of MessageComponentInteractionMetadataResponse from a dict
message_component_interaction_metadata_response_from_dict = MessageComponentInteractionMetadataResponse.from_dict(message_component_interaction_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


