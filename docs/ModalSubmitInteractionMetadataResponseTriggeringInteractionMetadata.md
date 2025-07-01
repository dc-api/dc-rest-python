# ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata


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

## Example

```python
from dc_rest.models.modal_submit_interaction_metadata_response_triggering_interaction_metadata import ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata from a JSON string
modal_submit_interaction_metadata_response_triggering_interaction_metadata_instance = ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata.from_json(json)
# print the JSON string representation of the object
print(ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata.to_json())

# convert the object into a dict
modal_submit_interaction_metadata_response_triggering_interaction_metadata_dict = modal_submit_interaction_metadata_response_triggering_interaction_metadata_instance.to_dict()
# create an instance of ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata from a dict
modal_submit_interaction_metadata_response_triggering_interaction_metadata_from_dict = ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata.from_dict(modal_submit_interaction_metadata_response_triggering_interaction_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


