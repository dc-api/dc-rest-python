# ApplicationCommandChannelOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | 
**description_localizations** | **Dict[str, str]** |  | [optional] 
**required** | **bool** |  | [optional] 
**channel_types** | **List[int]** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_channel_option import ApplicationCommandChannelOption

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandChannelOption from a JSON string
application_command_channel_option_instance = ApplicationCommandChannelOption.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandChannelOption.to_json())

# convert the object into a dict
application_command_channel_option_dict = application_command_channel_option_instance.to_dict()
# create an instance of ApplicationCommandChannelOption from a dict
application_command_channel_option_from_dict = ApplicationCommandChannelOption.from_dict(application_command_channel_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


