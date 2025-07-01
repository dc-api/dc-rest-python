# ModalSubmitInteractionMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**authorizing_integration_owners** | **Dict[str, str]** |  | 
**original_response_message_id** | **str** |  | [optional] 
**triggering_interaction_metadata** | [**ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata**](ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata.md) |  | 

## Example

```python
from dc_rest.models.modal_submit_interaction_metadata_response import ModalSubmitInteractionMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModalSubmitInteractionMetadataResponse from a JSON string
modal_submit_interaction_metadata_response_instance = ModalSubmitInteractionMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(ModalSubmitInteractionMetadataResponse.to_json())

# convert the object into a dict
modal_submit_interaction_metadata_response_dict = modal_submit_interaction_metadata_response_instance.to_dict()
# create an instance of ModalSubmitInteractionMetadataResponse from a dict
modal_submit_interaction_metadata_response_from_dict = ModalSubmitInteractionMetadataResponse.from_dict(modal_submit_interaction_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


