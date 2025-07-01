# ApplicationCommandOptionIntegerChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**value** | **int** |  | 

## Example

```python
from dc_rest.models.application_command_option_integer_choice import ApplicationCommandOptionIntegerChoice

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandOptionIntegerChoice from a JSON string
application_command_option_integer_choice_instance = ApplicationCommandOptionIntegerChoice.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandOptionIntegerChoice.to_json())

# convert the object into a dict
application_command_option_integer_choice_dict = application_command_option_integer_choice_instance.to_dict()
# create an instance of ApplicationCommandOptionIntegerChoice from a dict
application_command_option_integer_choice_from_dict = ApplicationCommandOptionIntegerChoice.from_dict(application_command_option_integer_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


