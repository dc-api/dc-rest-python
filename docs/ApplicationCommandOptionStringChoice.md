# ApplicationCommandOptionStringChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from dc_rest.models.application_command_option_string_choice import ApplicationCommandOptionStringChoice

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandOptionStringChoice from a JSON string
application_command_option_string_choice_instance = ApplicationCommandOptionStringChoice.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandOptionStringChoice.to_json())

# convert the object into a dict
application_command_option_string_choice_dict = application_command_option_string_choice_instance.to_dict()
# create an instance of ApplicationCommandOptionStringChoice from a dict
application_command_option_string_choice_from_dict = ApplicationCommandOptionStringChoice.from_dict(application_command_option_string_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


