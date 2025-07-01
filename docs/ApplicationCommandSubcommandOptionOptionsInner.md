# ApplicationCommandSubcommandOptionOptionsInner


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
**autocomplete** | **bool** |  | [optional] 
**choices** | [**List[ApplicationCommandOptionStringChoice]**](ApplicationCommandOptionStringChoice.md) |  | [optional] 
**min_value** | **float** |  | [optional] 
**max_value** | **float** |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_subcommand_option_options_inner import ApplicationCommandSubcommandOptionOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandSubcommandOptionOptionsInner from a JSON string
application_command_subcommand_option_options_inner_instance = ApplicationCommandSubcommandOptionOptionsInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandSubcommandOptionOptionsInner.to_json())

# convert the object into a dict
application_command_subcommand_option_options_inner_dict = application_command_subcommand_option_options_inner_instance.to_dict()
# create an instance of ApplicationCommandSubcommandOptionOptionsInner from a dict
application_command_subcommand_option_options_inner_from_dict = ApplicationCommandSubcommandOptionOptionsInner.from_dict(application_command_subcommand_option_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


