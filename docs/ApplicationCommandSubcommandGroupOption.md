# ApplicationCommandSubcommandGroupOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | 
**description_localizations** | **Dict[str, str]** |  | [optional] 
**required** | **bool** |  | [optional] 
**options** | [**List[ApplicationCommandSubcommandOption]**](ApplicationCommandSubcommandOption.md) |  | [optional] 

## Example

```python
from dc_rest.models.application_command_subcommand_group_option import ApplicationCommandSubcommandGroupOption

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandSubcommandGroupOption from a JSON string
application_command_subcommand_group_option_instance = ApplicationCommandSubcommandGroupOption.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandSubcommandGroupOption.to_json())

# convert the object into a dict
application_command_subcommand_group_option_dict = application_command_subcommand_group_option_instance.to_dict()
# create an instance of ApplicationCommandSubcommandGroupOption from a dict
application_command_subcommand_group_option_from_dict = ApplicationCommandSubcommandGroupOption.from_dict(application_command_subcommand_group_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


