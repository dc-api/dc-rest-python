# ApplicationCommandOptionNumberChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**value** | **float** |  | 

## Example

```python
from dc_rest.models.application_command_option_number_choice import ApplicationCommandOptionNumberChoice

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandOptionNumberChoice from a JSON string
application_command_option_number_choice_instance = ApplicationCommandOptionNumberChoice.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandOptionNumberChoice.to_json())

# convert the object into a dict
application_command_option_number_choice_dict = application_command_option_number_choice_instance.to_dict()
# create an instance of ApplicationCommandOptionNumberChoice from a dict
application_command_option_number_choice_from_dict = ApplicationCommandOptionNumberChoice.from_dict(application_command_option_number_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


