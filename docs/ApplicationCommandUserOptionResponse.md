# ApplicationCommandUserOptionResponse


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
from dc_rest.models.application_command_user_option_response import ApplicationCommandUserOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandUserOptionResponse from a JSON string
application_command_user_option_response_instance = ApplicationCommandUserOptionResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandUserOptionResponse.to_json())

# convert the object into a dict
application_command_user_option_response_dict = application_command_user_option_response_instance.to_dict()
# create an instance of ApplicationCommandUserOptionResponse from a dict
application_command_user_option_response_from_dict = ApplicationCommandUserOptionResponse.from_dict(application_command_user_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


