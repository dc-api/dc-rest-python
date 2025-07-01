# InteractionApplicationCommandAutocompleteCallbackIntegerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[Optional[ApplicationCommandOptionIntegerChoice]]**](ApplicationCommandOptionIntegerChoice.md) |  | [optional] 

## Example

```python
from dc_rest.models.interaction_application_command_autocomplete_callback_integer_data import InteractionApplicationCommandAutocompleteCallbackIntegerData

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionApplicationCommandAutocompleteCallbackIntegerData from a JSON string
interaction_application_command_autocomplete_callback_integer_data_instance = InteractionApplicationCommandAutocompleteCallbackIntegerData.from_json(json)
# print the JSON string representation of the object
print(InteractionApplicationCommandAutocompleteCallbackIntegerData.to_json())

# convert the object into a dict
interaction_application_command_autocomplete_callback_integer_data_dict = interaction_application_command_autocomplete_callback_integer_data_instance.to_dict()
# create an instance of InteractionApplicationCommandAutocompleteCallbackIntegerData from a dict
interaction_application_command_autocomplete_callback_integer_data_from_dict = InteractionApplicationCommandAutocompleteCallbackIntegerData.from_dict(interaction_application_command_autocomplete_callback_integer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


