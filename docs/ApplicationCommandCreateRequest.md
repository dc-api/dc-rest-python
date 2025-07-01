# ApplicationCommandCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**description_localizations** | **Dict[str, str]** |  | [optional] 
**options** | [**List[ApplicationCommandCreateRequestOptionsInner]**](ApplicationCommandCreateRequestOptionsInner.md) |  | [optional] 
**default_member_permissions** | **int** |  | [optional] 
**dm_permission** | **bool** |  | [optional] 
**contexts** | **List[int]** |  | [optional] 
**integration_types** | **List[int]** |  | [optional] 
**handler** | **int** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_create_request import ApplicationCommandCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandCreateRequest from a JSON string
application_command_create_request_instance = ApplicationCommandCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandCreateRequest.to_json())

# convert the object into a dict
application_command_create_request_dict = application_command_create_request_instance.to_dict()
# create an instance of ApplicationCommandCreateRequest from a dict
application_command_create_request_from_dict = ApplicationCommandCreateRequest.from_dict(application_command_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


