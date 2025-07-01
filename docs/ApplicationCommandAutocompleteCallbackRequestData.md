# ApplicationCommandAutocompleteCallbackRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[ApplicationCommandOptionStringChoice]**](ApplicationCommandOptionStringChoice.md) |  | [optional] 

## Example

```python
from dc_rest.models.application_command_autocomplete_callback_request_data import ApplicationCommandAutocompleteCallbackRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandAutocompleteCallbackRequestData from a JSON string
application_command_autocomplete_callback_request_data_instance = ApplicationCommandAutocompleteCallbackRequestData.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandAutocompleteCallbackRequestData.to_json())

# convert the object into a dict
application_command_autocomplete_callback_request_data_dict = application_command_autocomplete_callback_request_data_instance.to_dict()
# create an instance of ApplicationCommandAutocompleteCallbackRequestData from a dict
application_command_autocomplete_callback_request_data_from_dict = ApplicationCommandAutocompleteCallbackRequestData.from_dict(application_command_autocomplete_callback_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


