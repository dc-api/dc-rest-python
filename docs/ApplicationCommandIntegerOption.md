# ApplicationCommandIntegerOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | 
**description_localizations** | **Dict[str, str]** |  | [optional] 
**required** | **bool** |  | [optional] 
**autocomplete** | **bool** |  | [optional] 
**choices** | [**List[ApplicationCommandOptionIntegerChoice]**](ApplicationCommandOptionIntegerChoice.md) |  | [optional] 
**min_value** | **int** |  | [optional] 
**max_value** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_integer_option import ApplicationCommandIntegerOption

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandIntegerOption from a JSON string
application_command_integer_option_instance = ApplicationCommandIntegerOption.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandIntegerOption.to_json())

# convert the object into a dict
application_command_integer_option_dict = application_command_integer_option_instance.to_dict()
# create an instance of ApplicationCommandIntegerOption from a dict
application_command_integer_option_from_dict = ApplicationCommandIntegerOption.from_dict(application_command_integer_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


