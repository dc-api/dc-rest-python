# ApplicationCommandResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**application_id** | **str** |  | 
**version** | **str** |  | 
**default_member_permissions** | **str** |  | [optional] 
**type** | **int** |  | 
**name** | **str** |  | 
**name_localized** | **str** |  | [optional] 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | 
**description_localized** | **str** |  | [optional] 
**description_localizations** | **Dict[str, str]** |  | [optional] 
**guild_id** | **str** |  | [optional] 
**dm_permission** | **bool** |  | [optional] 
**contexts** | **List[int]** |  | [optional] 
**integration_types** | **List[int]** |  | [optional] 
**options** | [**List[ApplicationCommandResponseOptionsInner]**](ApplicationCommandResponseOptionsInner.md) |  | [optional] 
**nsfw** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_response import ApplicationCommandResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandResponse from a JSON string
application_command_response_instance = ApplicationCommandResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandResponse.to_json())

# convert the object into a dict
application_command_response_dict = application_command_response_instance.to_dict()
# create an instance of ApplicationCommandResponse from a dict
application_command_response_from_dict = ApplicationCommandResponse.from_dict(application_command_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


