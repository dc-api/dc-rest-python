# ApplicationCommandAttachmentOptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**name** | **str** |  | 
**name_localized** | **str** |  | [optional] 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | 
**description_localized** | **str** |  | [optional] 
**description_localizations** | **Dict[str, str]** |  | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_attachment_option_response import ApplicationCommandAttachmentOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandAttachmentOptionResponse from a JSON string
application_command_attachment_option_response_instance = ApplicationCommandAttachmentOptionResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandAttachmentOptionResponse.to_json())

# convert the object into a dict
application_command_attachment_option_response_dict = application_command_attachment_option_response_instance.to_dict()
# create an instance of ApplicationCommandAttachmentOptionResponse from a dict
application_command_attachment_option_response_from_dict = ApplicationCommandAttachmentOptionResponse.from_dict(application_command_attachment_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


