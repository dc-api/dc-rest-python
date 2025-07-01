# ApplicationCommandPatchRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**description_localizations** | **Dict[str, str]** |  | [optional] 
**options** | [**List[ApplicationCommandCreateRequestOptionsInner]**](ApplicationCommandCreateRequestOptionsInner.md) |  | [optional] 
**default_member_permissions** | **int** |  | [optional] 
**dm_permission** | **bool** |  | [optional] 
**contexts** | **List[int]** |  | [optional] 
**integration_types** | **List[int]** |  | [optional] 
**handler** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_patch_request_partial import ApplicationCommandPatchRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandPatchRequestPartial from a JSON string
application_command_patch_request_partial_instance = ApplicationCommandPatchRequestPartial.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandPatchRequestPartial.to_json())

# convert the object into a dict
application_command_patch_request_partial_dict = application_command_patch_request_partial_instance.to_dict()
# create an instance of ApplicationCommandPatchRequestPartial from a dict
application_command_patch_request_partial_from_dict = ApplicationCommandPatchRequestPartial.from_dict(application_command_patch_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


