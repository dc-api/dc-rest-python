# BasicMessageResponseInteractionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**authorizing_integration_owners** | **Dict[str, str]** |  | 
**original_response_message_id** | **str** |  | [optional] 
**target_user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**target_message_id** | **str** |  | [optional] 
**interacted_message_id** | **str** |  | 
**triggering_interaction_metadata** | [**ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata**](ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata.md) |  | 

## Example

```python
from dc_rest.models.basic_message_response_interaction_metadata import BasicMessageResponseInteractionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BasicMessageResponseInteractionMetadata from a JSON string
basic_message_response_interaction_metadata_instance = BasicMessageResponseInteractionMetadata.from_json(json)
# print the JSON string representation of the object
print(BasicMessageResponseInteractionMetadata.to_json())

# convert the object into a dict
basic_message_response_interaction_metadata_dict = basic_message_response_interaction_metadata_instance.to_dict()
# create an instance of BasicMessageResponseInteractionMetadata from a dict
basic_message_response_interaction_metadata_from_dict = BasicMessageResponseInteractionMetadata.from_dict(basic_message_response_interaction_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


