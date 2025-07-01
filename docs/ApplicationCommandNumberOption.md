# ApplicationCommandNumberOption


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
**choices** | [**List[ApplicationCommandOptionNumberChoice]**](ApplicationCommandOptionNumberChoice.md) |  | [optional] 
**min_value** | **float** |  | [optional] 
**max_value** | **float** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_number_option import ApplicationCommandNumberOption

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandNumberOption from a JSON string
application_command_number_option_instance = ApplicationCommandNumberOption.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandNumberOption.to_json())

# convert the object into a dict
application_command_number_option_dict = application_command_number_option_instance.to_dict()
# create an instance of ApplicationCommandNumberOption from a dict
application_command_number_option_from_dict = ApplicationCommandNumberOption.from_dict(application_command_number_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


