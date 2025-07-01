# InteractionApplicationCommandAutocompleteCallbackStringData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[Optional[ApplicationCommandOptionStringChoice]]**](ApplicationCommandOptionStringChoice.md) |  | [optional] 

## Example

```python
from dc_rest.models.interaction_application_command_autocomplete_callback_string_data import InteractionApplicationCommandAutocompleteCallbackStringData

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionApplicationCommandAutocompleteCallbackStringData from a JSON string
interaction_application_command_autocomplete_callback_string_data_instance = InteractionApplicationCommandAutocompleteCallbackStringData.from_json(json)
# print the JSON string representation of the object
print(InteractionApplicationCommandAutocompleteCallbackStringData.to_json())

# convert the object into a dict
interaction_application_command_autocomplete_callback_string_data_dict = interaction_application_command_autocomplete_callback_string_data_instance.to_dict()
# create an instance of InteractionApplicationCommandAutocompleteCallbackStringData from a dict
interaction_application_command_autocomplete_callback_string_data_from_dict = InteractionApplicationCommandAutocompleteCallbackStringData.from_dict(interaction_application_command_autocomplete_callback_string_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


