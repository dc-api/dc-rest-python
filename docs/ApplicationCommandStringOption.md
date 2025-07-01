# ApplicationCommandStringOption


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
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**choices** | [**List[ApplicationCommandOptionStringChoice]**](ApplicationCommandOptionStringChoice.md) |  | [optional] 

## Example

```python
from dc_rest.models.application_command_string_option import ApplicationCommandStringOption

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandStringOption from a JSON string
application_command_string_option_instance = ApplicationCommandStringOption.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandStringOption.to_json())

# convert the object into a dict
application_command_string_option_dict = application_command_string_option_instance.to_dict()
# create an instance of ApplicationCommandStringOption from a dict
application_command_string_option_from_dict = ApplicationCommandStringOption.from_dict(application_command_string_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


