# InteractionApplicationCommandAutocompleteCallbackNumberData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[Optional[ApplicationCommandOptionNumberChoice]]**](ApplicationCommandOptionNumberChoice.md) |  | [optional] 

## Example

```python
from dc_rest.models.interaction_application_command_autocomplete_callback_number_data import InteractionApplicationCommandAutocompleteCallbackNumberData

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionApplicationCommandAutocompleteCallbackNumberData from a JSON string
interaction_application_command_autocomplete_callback_number_data_instance = InteractionApplicationCommandAutocompleteCallbackNumberData.from_json(json)
# print the JSON string representation of the object
print(InteractionApplicationCommandAutocompleteCallbackNumberData.to_json())

# convert the object into a dict
interaction_application_command_autocomplete_callback_number_data_dict = interaction_application_command_autocomplete_callback_number_data_instance.to_dict()
# create an instance of InteractionApplicationCommandAutocompleteCallbackNumberData from a dict
interaction_application_command_autocomplete_callback_number_data_from_dict = InteractionApplicationCommandAutocompleteCallbackNumberData.from_dict(interaction_application_command_autocomplete_callback_number_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


