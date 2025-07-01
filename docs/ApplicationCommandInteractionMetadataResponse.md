# ApplicationCommandInteractionMetadataResponse


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

## Example

```python
from dc_rest.models.application_command_interaction_metadata_response import ApplicationCommandInteractionMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandInteractionMetadataResponse from a JSON string
application_command_interaction_metadata_response_instance = ApplicationCommandInteractionMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandInteractionMetadataResponse.to_json())

# convert the object into a dict
application_command_interaction_metadata_response_dict = application_command_interaction_metadata_response_instance.to_dict()
# create an instance of ApplicationCommandInteractionMetadataResponse from a dict
application_command_interaction_metadata_response_from_dict = ApplicationCommandInteractionMetadataResponse.from_dict(application_command_interaction_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


